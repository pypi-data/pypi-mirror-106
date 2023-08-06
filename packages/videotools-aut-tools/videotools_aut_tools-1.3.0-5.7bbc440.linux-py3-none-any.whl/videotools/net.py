"""
Module with network utilities
"""

# - csv formatted file columns
import abc
import errno
import json
import logging
import os
import socket
from argparse import ArgumentTypeError
from collections import namedtuple
from urllib.parse import urlparse

import ipinfo
import paramiko
import requests
import winrm
from jsonschema import validate
from stringcolor import cs
from tqdm import tqdm
from winrm.exceptions import InvalidCredentialsError
from winrm.transport import Transport

from videotools import APP_LOGLEVEL, COLOR_RED, COLOR_GREEN, get_resource_path
from videotools.model import ColoredException, ProgressBarScheduler, \
    MissingArgumentException, ProgressBar, Stats, MissingTokenException
from videotools.settings import IPINFO_TOKEN
from videotools.utils import check_path, DateTimeHelper

DEFAULT_TIMEOUT = 10
DEFAULT_SSH_PORT = 22
DEFAULT_WINRM_PORT = 5985

# -- csv format for ssh batch executions
# CSV_COL_OS = 0
# CSV_COL_HOSTNAME = 1
# CSV_COL_HOST = 2
# CSV_COL_PORT = 3
# CSV_COL_TIMEOUT = 4
# CSV_COL_USERNAME = 5
# CSV_COL_PASS_OR_KEYFILE = 6
#
# CSV_COLS_DICT = {CSV_COL_OS: 'os',
#                  CSV_COL_HOSTNAME: 'hostname',
#                  CSV_COL_HOST: 'host',
#                  CSV_COL_PORT: 'port',
#                  CSV_COL_TIMEOUT: 'timeout',
#                  CSV_COL_USERNAME: 'username',
#                  CSV_COL_PASS_OR_KEYFILE: 'password'}

# map for connections
# BOOL2STR_DICT = {True: 'OK', False: 'KO'}

# ipinfo details field names
IPINFO_FIELDS = {'IP': 'ip', 'HOSTNAME': 'hostname', 'CITY': 'city', 'REGION': 'region', 'COUNTRY': 'country',
                 'LOC': 'loc', 'ORG': 'org', 'POSTAL': 'postal', 'TIMEZONE': 'timezone', 'COUNTRY_NAME': 'country_name',
                 'LATITUDE': 'latitude', 'LONGITUDE': 'longitude'}

_logger = logging.getLogger('net')

# configure paramiko loglevel.
# handlers config in main appp's json config file
logging.getLogger("paramiko").setLevel(APP_LOGLEVEL)


# ---------------
#    EXCEPTIONS
# ---------------


class ServerNotAvailableException(ColoredException):
    """
    Exception launched when ip/hostname can not be reached
    """


class NoActiveSshConnException(ColoredException):
    """
    Exception launched when ssh connection is missing, or not active
    """

    def __init__(self, msg='ssh connection is not active', **kwargs):
        super().__init__(msg, **kwargs)


class ConnException(ColoredException):
    """
    Exception launched when a ssh connection can not be established
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, msg, **kwargs):
        super().__init__(msg, **kwargs)


class SshConnException(ConnException):
    """
    Exception launched when a ssh connection can not be established
    """

    def __init__(self, msg='Could no create a ssh connection', **kwargs):
        super().__init__(msg, **kwargs)


class WinRmConnException(ConnException):
    """
    Exception launched when a winrm connection can not be established
    """

    def __init__(self, msg='Could no create a winrm connection', **kwargs):
        super().__init__(msg, **kwargs)


class SshExecException(ColoredException):
    """
    Exception launched when there is an exception in a ssh command remote invocation
    """


class RemoteResultError(ColoredException):
    """
    Exception launched when there is an error in remote host during command execution
    """

    def __init__(self, stderr, **kwargs):
        super().__init__(f'Remote error occurred:\n\n\t {stderr}', **kwargs)
        self.stderr = stderr


class WrongCsvLineFormatError(ArgumentTypeError):
    """
    Exception launched when supplied csv line is not correct
    """
    LINE_FORMAT = 'hostname;host;port;timeout;username;password/keyfile;name1#command1;name2#command2...'

    def __init__(self, line):
        msg = cs(f'Wrong format for:\n\n{line}\n', COLOR_RED)
        msg += cs(f'\n\t -> {self.LINE_FORMAT}\n', COLOR_GREEN)
        super().__init__(msg)
        self.line = line


class WrongIpInfoFieldNameException(ColoredException):
    """
    Exception launched when supplied ipinfo field name is not correct
    """

    def __init__(self, fieldname):
        super().__init__("Supplied field name is not valid. Note: it's case unsensitive", fieldname=fieldname,
                         valid_names=str(IPINFO_FIELDS.values()))


class CouldNotGetIpInfoException(ColoredException):
    """
    Exception launched when can not get ip information from supplied ip address
    """

    def __init__(self, ipaddress):
        super().__init__("Could not get ipinfo from adress", ipaddress=ipaddress)


class CouldNotLoadFileFromUrl(ColoredException):
    """
    Exception when file can not be loaded from supplied url
    """


class WinrmExecException(ColoredException):
    """
    Exception launched when there is an exception in a winrm command remote invocation
    """


# -----------
#    LOGIC
# -----------

# -- net


def is_available(host, **kwargs):
    """
    Check port access to an ip
    :param host: Ip or fqdn of the node to check
    :param kwargs: optional arguments
            hostname: Name of the host
            port: SSH port number
            timeout: Timeout of the connection
            loginfo: Log result  at info level
          as_string: Instead of True/False, return OK/KO
    :return: A boolean wih the status of the check
    """
    hostname = kwargs.get('hostname', 'N/A')
    port = int(kwargs.get('port', DEFAULT_SSH_PORT))
    timeout = int(kwargs.get('timeout', DEFAULT_TIMEOUT))
    loginfo = kwargs.get('loginfo', True)

    assert host, 'Ip or fqdn is required'

    _logger.debug('checking access to port [%s] on ip [%s]...', port, host)

    try:
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sck.settimeout(timeout)
        sck.connect((host, port))
        if loginfo:
            _logger.info('checking hostname [%s] with ip [%s] and port [%s] : %s', hostname, host, port,
                         cs('OK', COLOR_GREEN))
        return True
    except socket.timeout:
        _logger.debug('\t connection timeout. Port [%s] is CLOSED at [%s]', port, host)
        if loginfo:
            _logger.error('checking [%s] with ip [%s] and port [%s] : KO', hostname, host, port)
        return False
    except socket.error as e:
        if e.errno == errno.ECONNREFUSED:
            _logger.debug('\t connection refused. Port [%s] is CLOSED at [%s]', port, host)
            if loginfo:
                _logger.error('checking [%s] with ip [%s] and port [%s] : KO', hostname, host, port)
        return False
    except Exception as e:
        _logger.debug('\t exception opening socket in port [%s] at address [%s]: \n\t\t *** %s ***', port, host, str(e))
        if loginfo:
            _logger.error('checking [%s] with ip [%s] and port [%s] : KO', hostname, host, port)
        return False
    finally:
        sck.close()


def get_httpfile_content(url, **kwargs):
    """
    Loads a file content from supplied url
    :param url: Url to load file from
    :param kwargs: Extra args
        progress (bool): If True, then progress bar is shown.
    """
    progress = kwargs.get('progress', False)

    _logger.debug('getting file content from [ %s ]', url)
    try:
        netloc = urlparse(url).netloc
        hostname_port = netloc.split(':')
        if len(hostname_port) > 1:
            host = hostname_port[0]
            port = int(hostname_port[1])
        else:
            host = hostname_port[0]
            port = 80
    except Exception as ex:
        raise CouldNotLoadFileFromUrl('Error parsing url', url=url)

    if not is_available(host, port=port):
        raise CouldNotLoadFileFromUrl('Url is not available', url=url)

    pbScheduler = ProgressBarScheduler(f'Downloading {os.path.split(url)[1]}', fake=not progress)
    pbScheduler.start()
    _response = requests.get(url)
    pbScheduler.quit()
    if not _response.ok:
        raise CouldNotLoadFileFromUrl(_response.content, url=url, status_code=_response.status_code)
    return _response.content


def _check_ipinfo_field(fieldname):
    """
    Checks if supplied fieldname is a valid
    """
    _logger.debug('checking ipinfo field [ %s ]', fieldname)
    if not fieldname in IPINFO_FIELDS.values():
        try:
            fieldname = IPINFO_FIELDS[fieldname.upper()]
        except (KeyError, TypeError) as err:
            raise WrongIpInfoFieldNameException(fieldname) from err
    return fieldname


def get_ipinfo(ip_address, **kwargs):
    """
    Gets information from supplied ip. The information can be retrieved as a dict, or as a json formatted string
    :param ip_address: IP to get information about
    :param fields: It's used as a fitler to get only information of supplied field names
    :return: A dictionary with full ip information,or only the information of supplied field names.
    """
    if not IPINFO_TOKEN:
        raise MissingTokenException('Missing token for ipinfo. Check with tools admin')

    # check fields and build correct list
    fields = list(map(_check_ipinfo_field, kwargs.get('fields', [])))

    try:
        handler = ipinfo.getHandler(IPINFO_TOKEN)
        details = handler.getDetails(ip_address).details

        # filter details if needed
        if fields:
            details = {key: value for key, value in details.items() if key in fields}
        return details
    except Exception as ex:
        raise CouldNotGetIpInfoException(ip_address) from ex


def get_ip_location(ip_adress):
    """
    Provides location of given ipaddress as latitude, longitude
    :param ip_address: IP to get information about
    :return: Return location as (latitude, longitude)
    """
    details = get_ipinfo(ip_adress, fields=['loc'])
    try:
        location = details['loc']
    except KeyError:
        location = '0,0'
    return location


def get_ip_countryname(ip_adress):
    """
    Provides country name of given ipaddress
    :param ip_address: IP to get information about
    """
    details = get_ipinfo(ip_adress, fields=['country_name'])
    return details['country_name']


# -- ssh

def new_ssh_connection(host, username, **kwargs):
    """
    Connects via SSH to the host using username/password or ssh key
    :param host: Ip or fqdn of the node to connect to
    :param username: Remote host username to login with
    :param kwargs: optional arguments
          password: User's password
           keyfile: File location that contains the ssh key
              port: ssh port
           timeout: Timeout of the connection
    """
    password = kwargs.get('password')
    keyfile = kwargs.get('keyfile')
    port = int(kwargs.get('port', DEFAULT_SSH_PORT))
    timeout = int(kwargs.get('timeout', DEFAULT_TIMEOUT))

    assert host and username and (password or keyfile), 'A host, username and password (or keyfile) is required'

    try:
        if not is_available(host, loginfo=False, **kwargs):
            raise ServerNotAvailableException(f'{host}:{port} can not be reached')

        # New ssh conn
        _logger.debug('\t creating new ssh connection:\n\t host: %s\n\t user: %s\n\t opts: %s', host, username,
                      str(kwargs))
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if password:
            _logger.debug('\t using password...')
            ssh_client.connect(host, username=username, password=password, timeout=timeout, port=port)
        else:
            _logger.debug('\t using pem key...')
            ssh_client.connect(host, username=username, key_filename=keyfile, timeout=timeout, port=port)
        return ssh_client
    except Exception as ex:
        raise SshConnException() from ex


def is_ssh_conn_active(ssh_conn):
    if not ssh_conn or ssh_conn.get_transport() is None or not ssh_conn.get_transport().is_active():
        raise NoActiveSshConnException()
    return True


# todo: add --dry-run logger output (option exists in main parent parser)
def ssh_exec(expression, **kwargs):
    """
    Runs an expression in a remote host using a SSH connection
    :param expression: Command/s to be executed in remote host
    :param kwargs: Optional arguments
        ssh_conn: Active ssh connection to use to perform remote expression execution
            host: IP to connect
        username: User's name
        password: User's password
         keyfile: File location that contains the ssh key
            port: ssh port
         timeout: Timeout of the connection
           close: If True, the connection is closed after execution (default). It's left opened otherwise
        no_output: The return will be OK or KO. Data will be logged but return will be simple, as OK, KO
    :return: The stdout of the remote expression if no err occurs, otherwise, a SshExecException is raised
    :raises:
               RemoteCommandExecutionError: When an error occurs during method invocation in remote host. Login
                                            was ok, but the result of comamnd execution was not
                          SshExecException: Method could not be executed in remote host
    """
    debug_args = {'cmd': expression}
    debug_args.update(kwargs)

    _logger.debug('executing ssh_exec:\n\t %s', debug_args)

    try:
        no_output = kwargs.get('no_output', False)

        # get an active ssh connection or create a new one
        ssh_conn = kwargs.get('ssh_conn')
        if not ssh_conn:
            kargs = kwargs.copy()
            ssh_conn = new_ssh_connection(kargs.pop('host'), kargs.pop('username'), **kargs)

        # check ssh connection is active (in case the connection was supplied as an optional arg)
        is_ssh_conn_active(ssh_conn)

        _logger.debug('\t executing command and waiting for end signal...')
        _, stdout, stderr = ssh_conn.exec_command(expression)

        # Wait until the command has finished. It'll return exec code result as an integer
        exec_status = stdout.channel.recv_exit_status()
        stdout = stdout.read().strip().decode("utf-8")
        stderr = stderr.read().strip().decode("utf-8")

        # any int value that is not 0 indicates an err in command execution
        if exec_status:
            if no_output:
                stderr = '**'
            raise RemoteResultError(stderr)

        if kwargs.get('close', True):
            _logger.debug('closing ssh connection...')
            ssh_conn.close()
            _logger.debug('\t Sucess')

        _logger.debug(f'\t stdout: {stdout}')
        if no_output:
            stdout = 'OK'
        return stdout

    except NoActiveSshConnException as ex:
        raise SshExecException('ssh conn is not active or is null', debug_args=debug_args) from ex
    except SshConnException as ex:
        raise SshExecException('could not create ssh connection', debug_args=debug_args) from ex
    except paramiko.BadHostKeyException as ex:
        raise SshExecException("SSH server's key did not match what we were expecting",
                               debug_args=debug_args) from ex
    except paramiko.AuthenticationException as ex:
        raise SshExecException('authentication failed', debug_args=debug_args) from ex
    except paramiko.SSHException as ex:
        raise SshExecException('failures in SSH2 protocol negotiation', debug_args=debug_args) from ex
    except socket.error as err:
        if ssh_conn:
            ssh_conn.close()
        raise SshExecException('socket IO error', debug_args=debug_args) from err
    except Exception as ex:
        # if an error ocurred during remote invocation, just raise the exceptio and handle it above
        if isinstance(ex, RemoteResultError):
            if kwargs.get('close', True):
                _logger.debug('closing ssh connection...')
                ssh_conn.close()
                _logger.debug('\t Success')
            raise ex
        if ssh_conn:
            ssh_conn.close()
        raise SshExecException('Unchecked exception', **debug_args) from ex


# --  winrm

def new_winrm_session(host, username, password, **kwargs):
    """
    Creates a new winrm session
    :param host: Target ip or fqdn
    :param username: User to log into remote system
    :param password: User password for session
    :param kwargs: Any extra arguments
           transport: Transport protocol for Winrm
          cert_check: Ignore certificate validation if False
          encryption: Encrypt messages if True
                port: ssh port
             timeout: Timeout of the connection
    :return: A winrm session
    """
    _transport = kwargs.get('transport', 'ntlm')
    _cert_check = kwargs.get('cert_check', True)
    _encryption = kwargs.get('encryption', 'auto')
    _port = kwargs['port'] = int(kwargs.get('port', DEFAULT_WINRM_PORT))
    kwargs['timeout'] = int(kwargs.get('timeout', DEFAULT_TIMEOUT))

    if not host or not username or not password:
        raise MissingArgumentException('A host, username and password are required')

    try:
        if not is_available(host, loginfo=False, **kwargs):
            raise ServerNotAvailableException(f'{host}:{_port} can not be reached')

        # New ssh conn
        _logger.debug('\t creating new winrm session:\n\t host: %s\n\t user: %s\n\t opts: %s', host, username,
                      str(kwargs))

        _host_conn = f'http://{host}:{_port}/wsman'

        _session = winrm.Session(_host_conn, auth=(username, password), transport=_transport)

        # make sure protocol does not fail with self signed certs
        if not _cert_check:
            _protocol = winrm.Protocol(endpoint=_host_conn,
                                       transport=_transport,
                                       username=username,
                                       password=password,
                                       server_cert_validation='ignore',
                                       message_encryption=_encryption)

            _session.protocol = _protocol
        return _session
    except Exception as ex:
        raise WinRmConnException() from ex


def winrm_exec(expression, **kwargs):
    """
    Runs an expression in a remote host using a WINRM connection
    :param expression: Command/s to be executed in remote host
    :param kwargs: Optional arguments
              session: An already created winrm session to use to perform remote expression execution
                 host: IP to connect
             username: User's name
             password: User's password
            transport: Transport protocol for Winrm
           cert_check: Ignore certificate validation if False
           encryption: Encrypt messages if True
                 port: ssh port
              timeout: Timeout of the connection
            no_output: The return will be OK or KO. Data will be logged but return will be simple, as OK, KO
           check_host: Check if host is available
    :return: The stdout of the remote expression if no err occurs, otherwise, a WinRmExecException is raised
    """
    debug_args = {'cmd': expression}
    debug_args.update(kwargs)

    _logger.debug('executing winrm:\n\t %s', debug_args)

    no_output = kwargs.get('no_output', False)
    session = kwargs.get('session')

    # If a session is provided, just use it
    if not session:
        kargs = kwargs.copy()
        kargs['port'] = kwargs.get('port', DEFAULT_WINRM_PORT)
        session = new_winrm_session(kargs.pop('host'), kargs.pop('username'), kargs.pop('password'), **kargs)
    else:
        # check supplied session is right
        assert isinstance(session, winrm.Session), cs('session has to be an instance of winrm.Session', COLOR_RED)
        _logger.debug('\t checking if supplied host in session is active...')
        _parsed = urlparse(session.url)
        _hostname = _parsed.hostname
        _port = _parsed.port
        if _hostname and _port:
            if not is_available(_hostname, port=_port, loginfo=False):
                raise WinRmConnException('Could not create winrm session', host=_hostname, port=_port,
                                         debug_args=debug_args)

    _logger.debug('\t executing powershell command and waiting for end signal...')
    # the response object, was three attributes: std_out, std_err and status_code
    _response = session.run_ps(expression)

    # Wait until the command has finished. It'll return exec code result as an integer
    exec_status = _response.status_code

    # any int value that is not 0 indicates an err in command execution
    if exec_status:
        stderr = _response.std_err.decode('utf-8')
        if no_output:
            stderr = '**'
        raise RemoteResultError(stderr)

    stdout = _response.std_out.decode('utf-8')
    _logger.debug(f'\t stdout: {stdout}')
    if no_output:
        stdout = 'OK'
    return stdout


class JsonSchemaValidated:
    """
    Class with common methods for any class built from a json dump, and which slots are wel defined.
    """
    __metaclass__ = abc.ABCMeta

    __slots__ = ()

    __slots_required__ = ()

    __schema__ = None

    def __new__(cls, *args, **kwargs):
        assert getattr(cls, '__slots__'), cs('__slots__ are required', COLOR_RED)
        for _name in cls.__slots_required__:
            if not hasattr(cls, _name) or getattr(cls, _name) is None:
                raise MissingArgumentException('Required argument not found', arg_name=_name)
        return super().__new__(cls)

    def __init__(self, **kwargs):
        self._validate(**kwargs)
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _validate(cls, **kwargs):
        with open(get_resource_path(cls.__schema__)) as _fb:
            _schema = json.loads(_fb.read())
        validate(instance=kwargs, schema=_schema)

    @classmethod
    def check(cls, instance):
        assert isinstance(instance, cls), cs(f'Supplied object is not a instance of [ {cls.__name__} ]')
        return instance

    def serialize(self):
        """
        Provides current class as a dictionary with field values
        :return: A dictionary with current serialized object
        """
        _dict = {}
        for _field in self.__slots__:
            _value = getattr(self, _field)
            if isinstance(_value, JsonSchemaValidated):
                _dict[_value] = _value.serialize()
            elif isinstance(_value, list):
                _dict[_field] = [o.serialize() if isinstance(o, JsonSchemaValidated) else o for o in _value]
            else:
                _dict[_field] = _value
        return _dict


# -- remote batch executors

class RemoteAuth(JsonSchemaValidated):
    """
    Abstract Class that represents some form of remote auth
    """

    __metaclass__ = abc.ABCMeta

    __slots__ = ()

    __slots_required__ = ('username',)

    __schema__ = 'remote_auth_schema.json'

    FIELD_NAMES = {'USERNAME': 'username', 'PASSWORD': 'password', 'KEYFILE': 'keyfile'}
    FIELDS = namedtuple('RemoteExecutorCommands', FIELD_NAMES.keys())(**FIELD_NAMES)

    @staticmethod
    def of(**kwargs):
        """
        Provides an instance of current class with supplied values
        :param kwargs: Any needed extra arguments
        :return: An instance of correct auth type class
        """
        if RemoteAuth.FIELDS.KEYFILE in kwargs.keys():
            return RemoteAuthSsh(**kwargs)
        else:
            return RemoteAuthBasic(**kwargs)


class RemoteAuthBasic(RemoteAuth):
    __slots__ = ('username', 'password')
    __slots_required__ = ('username', 'password')

    def get_auth_tuple(self):
        return self.username, self.password


class RemoteAuthSsh(RemoteAuth):
    __slots__ = ('username', 'keyfile')
    __slots_required__ = ('username', 'keyfile')


class RemoteConnectionException(ColoredException):
    """Exception launched when a remote connection could not be created"""


class RemoteCommand(JsonSchemaValidated):
    __slots__ = ('name', 'action')
    __slots_required__ = ('name', 'action')
    __schema__ = 'remote_cmd_schema.json'


class RemoteExecutor(JsonSchemaValidated):
    """
    Class that wraps command batch executions
    """
    __metaclass__ = abc.ABCMeta

    __slots__ = ('ip', 'hostname', 'port', 'timeout', 'auths', 'commands', 'connection', 'stats', 'results')

    __slots_required__ = ('ip',)

    __schema__ = 'remote_executor_schema.json'

    __os_type__ = None

    __default_port__ = None

    __default_timeout__ = None

    __stat_conn__ = 'connectivity'
    __stat_login__ = None

    logger = None

    FIELD_NAMES = {'IP': 'ip', 'HOSTNAME': 'hostname', 'PORT': 'port', 'TIMEOUT': 'timeout', 'OS': 'os',
                   'AUTHS': 'auths', 'COMMANDS': 'commands', 'CONNECTION': 'connection', 'STATS': 'stats',
                   'RESULTS': 'results'}
    FIELDS = namedtuple('RemoteExecutorCommands', FIELD_NAMES.keys())(**FIELD_NAMES)

    OS_NAME_LINUX = 'linux'
    OS_NAME_WINDOWS = 'windows'

    def __init__(self, **kwargs):
        """
        Creates an instance of this class
        :param ip: Target IP for remote commands
        :param kwargs: Extra arguments
            hostname: Name of the host, used for identification
                port: Port to be used instead of default one
             timeout: Timeout in seconds for connections, instead of default ones
               auths: An instance of RemoteAuth as a dictionary, or an array of these
            commands: An array of remote commands as dict, to be built
        """
        super().__init__(**kwargs)

        if not hasattr(self, 'hostname'):
            setattr(self, 'hostname', self.ip)

        self.connection = None
        self.stats = Stats()
        self.results = dict()

    @staticmethod
    def of(ip, os, **kwargs):
        """
        Creates an instance of corret type of remote executor based on supplied params
        :param ip: Target IP for remote commands
        :param os: Operating system of remote host
        :param kwargs: Extra arguments
            hostname: Name of the host, used for identification
               auths: An instance of RemoteAuth as a dictionary, or an array of these
            commands: An array of remote commands as dict, to be built
        :return: An instance of SshRemoteExecutor or WinRmRemoteExecutor
        """
        if not os:
            raise MissingArgumentException('Missing operating system type')
        elif not ip:
            raise MissingArgumentException('Missing target ip address')

        kwargs['ip'] = ip
        kwargs[RemoteExecutor.FIELDS.TIMEOUT] = kwargs.get(RemoteExecutor.FIELDS.TIMEOUT, DEFAULT_TIMEOUT)

        # -- auths
        kwargs[RemoteExecutor.FIELDS.AUTHS] = [RemoteAuth.of(**_auth) for _auth in
                                               kwargs.get(RemoteExecutor.FIELDS.AUTHS, [])]

        # -- commands
        kwargs[RemoteExecutor.FIELDS.COMMANDS] = [RemoteCommand(**_cmd) for _cmd in
                                                  kwargs.get(RemoteExecutor.FIELDS.COMMANDS, [])]

        if os == RemoteExecutor.OS_NAME_LINUX:
            kwargs[RemoteExecutor.FIELDS.PORT] = kwargs.get(RemoteExecutor.FIELDS.PORT,
                                                            SshRemoteExecutor.__default_port__)
            _instance = SshRemoteExecutor(**kwargs)
        else:
            kwargs[RemoteExecutor.FIELDS.PORT] = kwargs.get(RemoteExecutor.FIELDS.PORT,
                                                            WinRmRemoteExecutor.__default_port__)
            _instance = WinRmRemoteExecutor(**kwargs)
        return _instance

    def is_available(self, **kwargs):
        _logger.debug('wrapper: checking if host is available')
        if not is_available(self.ip, loginfo=True, **kwargs):
            raise ServerNotAvailableException('Server not available', hostname=kwargs.get('hostname'), ip=self.ip,
                                              port=kwargs.get('port'))
        return 'OK'

    def run_connectivity(self):
        _logger.info('checking connectivity to [%s]...', self.hostname)
        try:
            self.results[self.hostname][self.__stat_conn__] = self.is_available(hostname=self.hostname, port=self.port,
                                                                                timeout=self.timeout)
            self.stats.successUp(self.__stat_conn__)
        except ServerNotAvailableException:
            self.results[self.hostname][self.__stat_conn__] = 'KO'
            self.results[self.hostname][self.__stat_login__] = 'KO'
            self.stats.failureUp(self.__stat_conn__)
            self.stats.failureUp(self.__stat_login__)
            for _cmd in self.commands:
                self.results[self.hostname][_cmd.name] = 'KO'
                self.stats.failureUp(_cmd.name)
        return self.results[self.hostname][self.__stat_conn__]

    @abc.abstractmethod
    def connect(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def run_commands(self, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def close_connection(self):
        raise NotImplementedError()

    def exec(self):
        """
        Runs executor commands and return result or throw the correct exception
            raises:
                ServerNotAvailableException: If ip can not be reached

            return: A dictionary with results, where command names are keys, the result the values, and a Stats
                    instance with results is returned too
        """
        self.logger.debug('Starting new remote execution in host [ %s ]...', self.hostname)

        # create entry in results dictionary
        self.results[self.hostname] = dict()

        # -- connectivity
        _conn_result = self.run_connectivity()

        if _conn_result == 'KO' or not self.commands:
            _logger.debug('\t skipping remote execution, not command given')
            return self.results, self.stats

        try:
            # create a connection  to reuse in all commands
            self.connect()
        except ConnException:
            return self.results, self.stats

        # run commands
        self.run_commands()

        # close connection
        self.close_connection()

        # return results
        return self.results, self.stats


class SshRemoteExecutor(RemoteExecutor):
    """
    Class that wraps command batch executions using ssh
    """

    __os_type__ = RemoteExecutor.OS_NAME_LINUX

    __default_port__ = 22

    __default_timeout__ = 5

    __stat_conn__ = 'connectivity'
    __stat_login__ = 'login_linux'

    logger = logging.getLogger(f'ssh_executor')

    def connect(self):
        """
        Provides a new connection, trying all auth methods in case an error occurs
        """

        if self.connection:
            self.logger.debug('providing previous linux connection')
            return self.connection
        elif not self.auths:
            raise SshConnException('No auth method exists in executor')

        # try all auth methods if previous one fails
        for _auth in self.auths:
            try:
                _kwargs = dict()
                _kwargs[self.FIELDS.PORT] = self.port
                _kwargs[self.FIELDS.TIMEOUT] = self.timeout
                if isinstance(_auth, RemoteAuthSsh):
                    _kwargs[_auth.FIELDS.KEYFILE] = os.path.expanduser(_auth.keyfile)
                else:
                    _kwargs[_auth.FIELDS.PASSWORD] = _auth.password

                _logger.debug('creating new linux connection')
                self.connection = new_ssh_connection(self.ip, _auth.username, **_kwargs)

                # login is done when sshclient instance is created for linux hosts
                self.results[self.hostname][self.__stat_login__] = 'OK'
                self.stats.successUp(self.__stat_login__)
                return self.connection
            except SshConnException as ex:
                # if it's the last auth method, log error, add stats and results, and raise exception
                if self.auths.index(_auth) == (len(self.auths) - 1):
                    _logger.error('could not get connection with host [ %s ][ %s ]', self.hostname, self.ip)
                    self.results[self.hostname][self.__stat_login__] = 'KO'
                    self.stats.failureUp(self.__stat_login__)
                    for _cmd in getattr(self, self.FIELDS.COMMANDS):
                        self.results[self.hostname][_cmd.name] = 'KO'
                        self.stats.failureUp(_cmd.name)
                    raise ex

    def run_commands(self, **kwargs):
        """
        Executes current executor commands
        :param kwargs: Extra arguments
            progress: If True, then a progress bar is shown (default: True)
        """
        try:
            progress = kwargs.pop('progress')
        except KeyError:
            progress = True

        pbar = ProgressBar(total=len(self.commands), desc='Command', position=0, colour='green', fake=not progress)
        for _cmd in self.commands:
            _logger.info('executing __%s__...', _cmd.name)
            try:
                _rst = ssh_exec(_cmd.action, ssh_conn=self.connection, no_output=True, close=False, **kwargs)
                # increase success counter and save results
                self.results[self.hostname][_cmd.name] = _rst
                self.stats.successUp(_cmd.name)
            except SshExecException:
                _logger.error('could not execute [ %s ]\n\t on host [ %s ]', _cmd.name, self.hostname)
                self.results[self.hostname][_cmd.name] = 'KO'
                self.stats.failureUp(_cmd.name)
            except RemoteResultError as err:
                _logger.debug('remote error in command [ %s ]\n\t on host [ %s ]', _cmd.name, self.hostname)
                self.results[self.hostname][_cmd.name] = err.stderr
                self.stats.failureUp(_cmd.name)
            except Exception as ex:
                _logger.exception('Unchecked exception')
                self.results[self.hostname][_cmd.name] = str(ex)
                self.stats.failureUp(_cmd.name)
            finally:
                pbar.update(1)
        pbar.close()

    def close_connection(self):
        if self.connection:
            self.logger.debug('\t closing connection...')
            self.connection.close()


class WinRmRemoteExecutor(RemoteExecutor):
    """
    Class that wraps command batch executions using ssh
    """

    __os_type__ = RemoteExecutor.OS_NAME_LINUX

    __default_port__ = 5985

    __default_timeout__ = 5

    __stat_conn__ = 'connectivity'
    __stat_login__ = 'login_windows'

    logger = logging.getLogger(f'winrm_executor')

    def connect(self):
        """
        Provides a new connection, trying all auth methods in case an error occurs
        """
        self.logger.debug('reused connections not implemented in winrm. Skipping connect...')

    def run_commands(self, **kwargs):
        """
        Executes current executor commands
        :param kwargs: Extra arguments
            progress: If True, then a progress bar is shown (default: True)
        """
        try:
            progress = kwargs.pop('progress')
        except KeyError:
            progress = True

        pbar = ProgressBar(total=len(self.commands), desc='Command', position=0, colour='green', fake=not progress)
        win_logged = False
        update_login = False
        for _auth in self.auths:
            try:
                _kwargs = dict()
                _kwargs[self.FIELDS.PORT] = self.port
                _kwargs[self.FIELDS.TIMEOUT] = self.timeout
                _kwargs[_auth.FIELDS.PASSWORD] = _auth.password
                for _cmd in self.commands:
                    try:
                        _logger.info('new winrm command [ %s ]...', _cmd.name)
                        _rst = winrm_exec(_cmd.action, ssh_conn=self.connection, no_output=True, **kwargs)

                        # login is done when command is executed in winrm
                        # increase success counter and save results
                        self.results[self.hostname][_cmd.name] = _rst
                        self.stats.successUp(_cmd.name)
                        update_login = True
                    except RemoteResultError as err:
                        _logger.debug('remote error in command [ %s ]\n\t on host [ %s ]', _cmd.name, self.hostname)
                        self.results[self.hostname][_cmd.name] = err.stderr
                        self.stats.failureUp(_cmd.name)
                        update_login = True
                    finally:
                        pbar.update(1)
                        if update_login and not win_logged:
                            self.results[self.hostname][self.__stat_login__] = 'OK'
                            self.stats.successUp(self.__stat_login__)
                            win_logged = True
                        if self.results[self.hostname][self.__stat_login__] == 'OK' and \
                                self.commands.index(_cmd) == (len(self.commands) - 1):
                            return
            except InvalidCredentialsError as icerr:
                # if it's the last auth method, log error, add stats and results, and raise exception
                if self.auths.index(_auth) == (len(self.auths) - 1):
                    raise Exception() from icerr
            except Exception:
                _logger.error('could not establish connection with host [ %s ][ %s ]', self.hostname, self.ip)
                self.results[self.hostname][self.__stat_login__] = 'KO'
                self.stats.failureUp(self.__stat_login__)
                for _cmd in self.commands:
                    self.results[self.hostname][_cmd.name] = 'KO'
                    self.stats.failureUp(_cmd.name)
                return

    def close_connection(self):
        """
        Not implemented in winrm connections
        """
        self.logger.debug('no pre-created connections in winrm. Skip closing...')


class BatchExecutor(JsonSchemaValidated):
    """
    Class that wraps command batch executions
    """

    __slots__ = ('date', 'version', 'service', 'env', 'executors')

    __slots_required__ = __slots__

    __schema__ = 'batch_executor_schema.json'

    logger = logging.getLogger('batch_exec')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # create remote executors per host
        setattr(self, 'executors', [RemoteExecutor.of(_hst.pop('ip'), _hst.pop('os'), **_hst) for _hst in
                                    getattr(self, 'executors')])

    def of(batch_file):
        """
        Creates a new instance of BatchExecutor from supplied batchfile
        :param batchfile: Json formmated file following a known batchfile schema
        :return: Provides two dictionaries, one with results from commands, and another one with stats of those commands
        """
        batch_file = check_path(batch_file, extensions=['json'])

        _logger.debug('loading new batch file %s', batch_file)
        with open(batch_file) as _fb:
            _content = json.loads(_fb.read())

        # load main props
        _kwargs = dict()
        _kwargs['date'] = _content['date']
        _kwargs['version'] = _content['version']
        _kwargs['service'] = _content['service']
        _kwargs['env'] = _content['env']
        _kwargs['executors'] = _content['hosts']

        return BatchExecutor(**_kwargs)

    def print(self, results):
        """
        Prints results from supplied dictionary
        :param results: A dictionary with remote executors results in all hosts
        """
        print('-' * 100)
        print(f'{"HOSTNAME":^25}{"COMMAND":^50}{"RESULT":^30}')
        print('-' * 100)
        for _hostname, _rsts in results.items():
            print(f'\t{cs(_hostname, "yellow2"):<25}')
            for _name, value in _rsts.items():
                print(f'{"" * 25:<25}{_name:^50}{value:^30}')
        print('-' * 100)
        print()

    def exec(self, **kwargs):
        """
        Runs executor commands from supplied batch_file
        :param kwargs: Extra arguments
            progress: If True, then a progress bar is shown (default: True)
               short: Don't print results, only stats
            filename: If supplied, this file will be used for results, instead of default one
        """
        progress = kwargs.get('progress', True)
        short = kwargs.get('short', False)

        # global results and stats
        stats = Stats()
        results = dict()

        # progress bar
        pbar = ProgressBar(total=len(self.executors), desc='Host', position=0, colour='blue', fake=not progress)
        for executor in self.executors:
            _rsts, _sts = executor.exec()
            results.update(_rsts)
            stats.update(_sts)
            pbar.update(1)
        pbar.close()

        if not short:
            self.print(results)
        stats.print()
