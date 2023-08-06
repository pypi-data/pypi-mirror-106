"""
Module with convenience methods to perform operations on cdn infrastructure
"""
import abc
import json
import logging
import os
import re

import yaml
from jsonschema import validate
from stringcolor import cs
from tqdm import tqdm

from videotools import COLOR_YELLOW, COLOR_BLUE, COLOR_GREEN, get_resource_path, COLOR_RED, COLOR_GRAY, APP_HOME_DIR
from videotools.model import ColoredException, ProgressBarScheduler, MissingArgumentException, ProgressBar
from videotools.net import get_httpfile_content, get_ip_location, CouldNotGetIpInfoException, RemoteExecutor, \
    DEFAULT_SSH_PORT
from videotools.settings import ST2_PRO_COMMANDS, ST2_PRO_AUTHS, CONFIG_FIELDS
from videotools.utils import FileNotExistsError, check_path, input_wait, DateTimeHelper

# -- buckets
# 42988|null|ES-112-HLSV4-GR-MDEPORTES|MDEPORTES|NPantallas
# 43611|null|ES-198-SS-GR-MEZZO|MEZZO|NPantallas
LIVE_BUCKETS_CUSTOMERS = ['NPantallas.es',
                          'GVP_PRO_BR_PER_LIVE.GVP_VIVO.com',
                          'GVP_PRO_LT_LUR_LIVE.COM',
                          'MovistarClick.com',
                          'medianetworks.com',
                          'GVP_PRO_LT_LUR2_LIVE.com',
                          'GVP_PRO_AR_BAL_LIVE.COM',
                          'GVP_PRO_LT_CH_LIVE.COM',
                          'GVP_PRO_CO_CHA_LIVE.COM',
                          'PRO_TERRA_EXTERNAL']

# 44239|NPantallas
# 44250|NPantallas
# 44251|NPantallas
# 44303|NPantallas
VOD_BUCKETS_CUSTOMERS = ['aytoMadrid', 'cofreacs', 'delivery_iptv', 'GVP_SW_IPTV', 'GVP_TASA_MEDIA', 'medianetworks',
                         'NPantallas', 'TDigital', 'TEDxTelefonica', 'TelefonicaSAGVP', 'TelefonicaSAGVPAmerica',
                         'Yomvi', 'GVP_PRO_VOD_EXTERNAL_USECASES', 'ChileACS', 'PRO_TERRA_EXTERNAL', 'livingapps',
                         'PRO_MOVISTAR_GO_EXTERNAL', 'publicidad', 'servadicionales', 'vodclientui',
                         'Packager_downloader']

_logger = logging.getLogger('cdn')


class MissingGpsDataFile(ColoredException):
    """
    Exception launched when gps data file can not be found
    """

    def __init__(self, _gpsdatafile):
        super().__init__('Missing gps data file', _file=_gpsdatafile)


class CouldNotLoadGpsDataFile(ColoredException):
    """
    Exception launched when gps data file can not be loaded for some reason
    """


class WrongCsvFormatException(ColoredException):
    """
    Exception launched when supplied string is not in csv format
    """

    def __init__(self, txt):
        super().__init__('Wrong csv format. It should be "key1:value1,value2;key2;value2;key3:value..." or '
                         'key1;key2;key3;...',
                         text=txt)


class WrongEnvironmentException(ColoredException):
    """
    Exception launched when supplied environment is not a supported one
    """

    def __init__(self, env_name):
        super().__init__('Supplied environment is not supported', env_name=env_name)


class CouldNotBuildInventoryException(ColoredException):
    """
    Exception launched when inventory can not be build with supplied content
    """


class WrongInventoryException(ColoredException):
    """
    Exception launched when supplied inventory has not correct keys
    """


class NodeNotFoundError(ColoredException):
    """
    Exception launched when certain searched node is not found
    """


class CouldNotFindFieldException(ColoredException):
    """
    Exception launched when supplied field name is not found in inventory or inventory filter fields
    """


# -- logic


# -- inventories


class InventoryEnv:
    """
    Class that represents an environment of certain inventory
    """

    def __init__(self, name, **kwargs):
        """
        :param name: Name of environment
        :param source: Location of original content for this environment
        :param local: Location of local content for this environment
        :param kwargs: Any extra args that can be used in  this environment
            source: original content  location
             local: already local built inventory location
        """
        self.name = name
        self.service = kwargs.pop('service')
        self.source = kwargs.pop('source')
        self.local = kwargs.pop('local')

        try:
            self.home = kwargs.pop('home')
        except KeyError:
            self.home = self.service

        self.home = os.path.join(APP_HOME_DIR, self.home)

        # create paths
        if not os.path.exists(self.home):
            self.logger.debug('\t creating [ %s ]...', self.home)
            os.makedirs(self.home)

        # set the rest of args
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    def is_valid(self, name):
        return name == self.name

    def _exists(self, _name):
        try:
            check_path(os.path.join(self.home, _name))
            return True
        except FileNotExistsError:
            return False

    def get_local(self, **kwargs):
        """
        Provides local file from environment, if exists
        :param kwargs: Extra args
            version: If given, replace VERSION in local string with supplied version value
            nocheck: No check if file exists, just provide final name
        """
        version = kwargs.get('version', '')
        _file = os.path.join(self.home, self.local).replace('VERSION', version)
        if kwargs.get('nocheck', False):
            return _file
        return check_path(_file)

    def get_source(self, **kwargs):
        """
        Provides source content from environment, if exists
        :param kwargs: Extra args
            version: If given, replace VERSION in source with supplied version value
            nocheck: No check if filepath exists, just provide file name
        """
        version = kwargs.get('version', '')
        _file = self.source
        if _file.startswith('http'):
            return _file.replace('VERSION', version)

        _file = os.path.join(self.home, _file).replace('VERSION', version)
        if kwargs.get('nocheck', False):
            _file = check_path(_file)
        return _file

    def is_source_local(self):
        return self._exists(self.source)


class InventoryHost:
    """
    Class that encapsulates the concept of host in any inventory
    """

    __metaclass__ = abc.ABCMeta

    # inventory service name. This host can only be used in this kind of service
    __service__ = None

    # host fields
    __slots__ = ()

    # dictionary with len of inventory fields. It'll be used for printing content
    __slots_len__ = None

    # list of fields with IP information
    __slots_ip__ = None

    # Default sorting field in inventory
    __slots_sort__ = None

    KEY_IPADDRESS = 'ipaddress'
    KEY_WINDOWS = 'windows'
    KEY_LINUX = 'linux'

    logger = None

    def __new__(cls, *args, **kwargs):
        for _name in ('__service__', '__slots__', '__slots_len__', '__slots_ip__', '__slots_sort__', 'logger'):
            assert getattr(cls, _name), cs(f'Missing required inventory class field {_name}', COLOR_RED)
        return super().__new__(cls)

    def get_dict(self):
        """
        Provides current inventory host dictionary with field values
        :return: A dictionary with current values
        """
        _dict = {}
        for _field in self.__slots__:
            _dict[_field] = getattr(self, _field)
        return _dict

    def filter(self, csvfilter, **kwargs):
        """
        Filters current inventory host values using supplied csvfilter
        :param csvfilter: String to be used as filter. It's a CSV formatted line with key:value pairs to match in
            inventory. If key:value pairs are found, a dictionary is returned. If only key values are provided
            (separated by semicolon too), an array is returned, for example: field:value;field2:value2...
            or FIELD;FIELD2;FIELD3... field names can be uppercase or lowercase, it doesn't matter
            Multiple values can be provided for filtering as key1:value1,value2;key2:value1,value2...'
        :param kwargs: Any extra arguments
                case: If given, filtering will be done using case sensitive matching
        :return:  If a filter by key:value is supplied, current host dictionary is return if supplied values are
        found in host, else, None is returned. If a list of keys is supplied as filter, then current host's dictionary
        with only supplied keys is returned
        """
        if not csvfilter:
            self.logger.debug('skipping filtering, no filter provided')
            return self
        elif not isinstance(csvfilter, str) and not isinstance(csvfilter, dict):
            raise WrongCsvFormatException('csvfilter needs to be a dcitionary or a csv well formatted string')

        csvfilter = self.new_filter(csvfilter)

        case = kwargs.get('case', False)
        if case:
            self.logger.debug('\t case sensitive filtering enabled')

        # -- filter by key:value
        # check if all filter values are found in dict to be filtered
        self.logger.debug('\t filtering by key:value pairs in filter %s', csvfilter)
        for _fkey, _fvalue in csvfilter.items():
            _fvalue = [i for i in _fvalue if isinstance(_fvalue, list)] or [_fvalue]
            try:
                _dvalue = getattr(self, _fkey)
            except KeyError:
                self.logger.warning('Filter key [ %s ] not found in host %s', _fkey, self.__slots__)
                return None

            found = False
            for _fv in _fvalue:
                if not case:
                    _fv = _fv.upper()
                    _dvalue = _dvalue.upper()
                # check if dict contains filter value, as soon as there's one match, we exit loop
                if _fv in _dvalue:
                    found = True
                    break
            if not found:
                self.logger.debug('\t filtering value [ %s:%s ] not found in host value [ %s ]', _fkey, _fv, _dvalue)
                return None
        self.logger.debug('\t\t host filtering values found')
        return self

    def print(self, **kwargs):
        """
        Prints current host values, formatting if necessary
        :param kwargs: Extra arguments
              info: Print hosts values as info summary, instead of a line. Supplied value is printed in green
           columns: If given, only given field values will be printed
        """
        info = kwargs.get('info')
        columns = self.get_columns_filter(kwargs.get('columns', []))

        # print just this host info
        if info:
            print('-' * 80)
            print(cs('Node info:', COLOR_YELLOW))
            print()
            _slots = list(self.__slots__)
            _slots.insert(0, '__service__')
            for _key in _slots:
                _line = cs(f'{_key.strip("_"):>30}:', COLOR_BLUE)
                _value = getattr(self, _key)
                if info in _value:
                    _line += cs(f'\t{_value:<40}', COLOR_GREEN)
                else:
                    _line += cs(f'\t{_value:<40}', COLOR_GRAY)
                print(_line)
            print('-' * 80)
            return

        # print line for a table
        _line = ''
        for _hdr in self.__slots__:
            if columns and _hdr not in columns:
                self.logger.debug('\t skipping field [ %s ], not in filter [ %s ]', _hdr, columns)
                continue
            _line += '{:^{width}}'.format(getattr(self, _hdr), width=self.__slots_len__[_hdr])
        print(_line)

    @classmethod
    def get_columns_filter(cls, columns):
        """
        Provides final columns filter based on supplied columns
        """
        columns = columns or []

        # add hostname and interface columns always
        _slots = ['hostname']
        _slots.extend(cls.__slots_ip__)
        for _slt in _slots:
            if _slt not in columns:
                columns.append(_slt)
        return columns

    @classmethod
    def get_headers_total_length(cls, **kwargs):
        """
        Gives the total length of the headers to be print
        :param kwargs: Extra arguments
           columns: If given, only given field values will be printed
        """
        columns = cls.get_columns_filter(kwargs.get('columns', []))

        total_length = 0
        for _h in cls.__slots__:
            if columns and _h not in columns:
                continue
            total_length += cls.__slots_len__[_h]
        return total_length

    @classmethod
    def print_headers(cls, **kwargs):
        """
        Prints current host headers
        :param kwargs: Extra arguments
           columns: If given, only given field values will be printed
        """
        columns = cls.get_columns_filter(kwargs.get('columns', []))

        _headers = ''
        for _hdr in cls.__slots__:
            if columns and _hdr not in columns:
                cls.logger.debug('\t skipping header [ %s ], not in filter %s', _hdr, columns)
                continue
            _txt = _hdr
            if _hdr.startswith(f'{cls.KEY_IPADDRESS}_'):
                _txt = _hdr.split(f'{cls.KEY_IPADDRESS}_')[1]
            _headers += '{:^{width}}'.format(_txt, width=cls.__slots_len__[_hdr])
        print(_headers)

    @classmethod
    def check_field_valid(cls, fieldname):
        """
        Checks that supplied field name exists in fields list
        :param fieldname: Name of the field to check
        :return: True if valid. A CouldNotFindFieldException is thrown otherwise
        """
        try:
            # helper for simple ipaddress expressions:
            _fieldname = fieldname.lower()
            try:
                return next(filter(lambda x: x.endswith(_fieldname) and not _fieldname.startswith(cls.KEY_IPADDRESS),
                                   cls.__slots_ip__))
            except StopIteration:
                if _fieldname not in cls.__slots__:
                    raise KeyError()
            return _fieldname
        except KeyError:
            raise CouldNotFindFieldException('supplied field name is not valid', field=fieldname,
                                             valid_fields=str(cls.__slots__))

    @classmethod
    def check_filter(cls, csvfilter):
        """
        Checks that supplied value for a csv filter is valid for current host type
        :return: The value if valid, a CouldNotFindFieldException is thrown otherwise
        """
        if not csvfilter:
            return None

        cls.logger.debug('checking if csv filter value is valid: %s', csvfilter)

        # if it's a list
        if isinstance(csvfilter, list):
            for item in csvfilter:
                csvfilter[csvfilter.index(item)] = cls.check_field_valid(item)
            return csvfilter

        # then, it has to be a dict
        _csvfilter = {}
        for _key, _value in csvfilter.items():
            _csvfilter[cls.check_field_valid(_key)] = _value
        return _csvfilter

    @classmethod
    def new_filter(cls, csv_text):
        """
        Builds a new filter with supplied csv formatted string.
        WARN: ONLY valid for String filtering!!
        :param csv_text: String to be used as filter. It's a CSV formatted line with key:value pairs to match in
            inventory. If key:value pairs are found, a dictionary is returned. If only key values are provided
            (separated by semicolon too), an array is returned, for example: field:value;field2:value2...
            or FIELD;FIELD2;FIELD3... field names can be uppercase or lowercase, it doesn't matter
            Multiple values can be provided for filtering as key1:value1,value2;key2:value1,value2...'
        :return: An array or a dictionary  with generated filtering values
        """
        if not csv_text:
            return None

        # new instance
        if isinstance(csv_text, list) or isinstance(csv_text, dict):
            cls.logger.debug('building csv filter with supplied list or dict...')
            return cls.check_filter(csv_text)

        assert isinstance(csv_text, str), cs('Supplied csv_text must be a csv formatted string', COLOR_RED)

        cls.logger.debug('building csvfilter from __%s__', csv_text)

        # remove any missing ; from ends of the line
        csv_text = csv_text.lstrip(';').rstrip(';')

        try:
            cls.logger.debug('\t checking if keyvalue pairs separator is [ ; ]...')

            # -- array filter
            _value = None

            # wrong filter:  'key1;value1,value2'
            if ';' in csv_text and ',' in csv_text and ':' not in csv_text:
                raise WrongCsvFormatException(csv_text)
            if ';' in csv_text and ':' not in csv_text:  # array of keys separated by semicolon 'key1;key2;key3'
                _value = csv_text.split(';')
                cls.logger.debug('\t returning array of filter keys %s', _value)
            elif ';' not in csv_text and ':' not in csv_text:  # single key   'key1'
                _value = [csv_text.strip()]
                cls.logger.debug('\t returning single key array %s', )

            # return array of values if given values are valid
            if _value:
                return cls.check_filter([_v.strip() for _v in _value])

            # -- dictionary filter
            _fdict = {}

            # split values
            # Since it's a dict, all keys must specify a value, or an exception is raised
            for _tup in csv_text.split(';'):
                cls.logger.debug('\t checking if [ : ] separator exists in each found key:value pairs...')
                _keyvalue = _tup.split(':')
                if len(_keyvalue) == 1 or _keyvalue[1] == '':
                    raise
                cls.logger.debug('\t key and value found, checking if multiple values are given...')
                _key = _keyvalue[0].strip()
                _value = _keyvalue[1].split(',')
                if len(_value) > 1:
                    cls.logger.debug('\t\t multiple values found, adding list %s ...', _value)
                    _fdict[_key] = [_v.strip() for _v in _value if _v]
                else:
                    cls.logger.debug('\t\t single value found, adding %s ...', _value[0])
                    _fdict[_key] = _value[0].strip()
            return cls.check_filter(_fdict)
        except Exception:
            raise WrongCsvFormatException(csv_text)

    @classmethod
    def of(cls, **kwargs):
        """
        Builds an instance of certain inventory host with supplied field values. If wrong fields are supplied
        a CouldNotFindFieldException is thrown
        :param kwargs: Dictionary with host values
        """
        cls.logger.debug('building new host with %s', kwargs)
        _instance = cls()
        for _fieldname, _fieldvalue in kwargs.items():
            setattr(_instance, _instance.check_field_valid(_fieldname), _fieldvalue)
        return _instance


class Inventory:
    """
    Class that encapsulates all functionality expected in certain service inventory
    """
    __metaclass__ = abc.ABCMeta

    # inventory service name
    __service__ = None

    # names of inventory fields
    __slots__ = ('date', 'hosts', 'env', 'version')

    # Array with InventoryEnvironment instances
    __environments__ = None

    __environment_default__ = None

    # Host types for current inventory
    __host_type__ = None

    __version_required__ = None

    __expires__ = None

    logger = None

    VERSION_PATTERN = re.compile(r'\d+\.\d+\.\d+')

    def __new__(cls, *args, **kwargs):
        for _name in ('__service__', '__slots__', '__environments__', '__host_type__', '__version_required__',
                      '__environment_default__', '__expires__', 'logger'):
            assert hasattr(cls, _name), cs(f'Missing required inventory class field {_name}', COLOR_RED)
        return super().__new__(cls)

    def __init__(self, env, **kwargs):
        self.env = self.check_environment(env)
        self.date = DateTimeHelper.short_date()

        try:
            self.version = kwargs['version']
        except KeyError:
            if self.__version_required__:
                raise MissingArgumentException('Version is required for this inventory service',
                                               service=self.__service__)
            else:
                self.version = None
        self.hosts = []

    def load(self, **kwargs):
        """
        Tries to load content from local source. It if does not exists,a new inventory is built and persisted to
        local location.
        :param kwargs: Extra arguments
            source: If supplied, inventory is loaded from supplied source
        """
        # check if source was supplied in kwargs
        try:
            _file = kwargs.pop('source')
        except KeyError:
            _file = None

        # try to load default source, if no file was provided
        if not _file:
            try:
                _file = self.env.get_local(version=self.version)
                _logger.debug('checking if local file  [ %s ] exists...', _file)
            except FileNotExistsError:
                self.logger.info('\t not found, building...')
                return self.build(**kwargs)
        else:
            _logger.info('checking if supplied file [ %s ] exists...', _file)
            _file = check_path(_file, extensions=['json'])

        # load content
        _logger.debug('\t loading...')
        with open(_file) as _fb:
            _idict = json.loads(_fb.read())

        _logger.debug('\t checking inventory format...')
        self.check_inventory(_idict)

        # update file if older than 24h
        _logger.debug('\t checking if expired...')
        if DateTimeHelper.days_between(_idict['date'], DateTimeHelper.short_date()) < 1 or not self.__expires__:
            self.clone_from(_idict)
            return
        _logger.info('\t expired inventory, building...')
        return self.build(**kwargs)

    def get_inventory(self, **kwargs):
        """
        Provides current inventory content as a dictionary
        :param kwargs: Any extra arguments
            csvfilter: String to be used as filter for hosts. It's a CSV formatted line with key:value pairs
            to match each host with. If key:value pairs are found, a dictionary is returned. If only key values
            are provided (separated by semicolon too), an array is returned, for example: field:value;field2:value2...
            or FIELD;FIELD2;FIELD3... field names can be uppercase or lowercase, it doesn't matter
            Multiple values can be provided for filtering as key1:value1,value2;key2:value1,value2...'

            case: If given, filtering will be done using case sensitive matching
        :return: A dictionary with inventory content
        """
        return {'date': self.date,
                'version': self.version or 'unknown',
                'service': self.__service__,
                'env': self.env.name,
                'hosts': self.get_hosts(**kwargs)}

    def get_hosts(self, **kwargs):
        """
        Provides the hosts list of current inventory
        :param kwargs: Any extra arguments
            csvfilter: String to be used as filter for hosts. It's a CSV formatted line with key:value pairs
            to match each host with. If key:value pairs are found, a dictionary is returned. If only key values
            are provided (separated by semicolon too), an array is returned, for example: field:value;field2:value2...
            or FIELD;FIELD2;FIELD3... field names can be uppercase or lowercase, it doesn't matter
            Multiple values can be provided for filtering as key1:value1,value2;key2:value1,value2...'

            case: If given, filtering will be done using case sensitive matching
            sort: If given, inventory will be sorted ascending by given column name, if exists. Default sorting
                  field is __field_sort__ value
        :return: A list with current inventory hosts, filtered and/or sortered
        """
        sort_field = self.__host_type__.check_field_valid(kwargs.get('sort', self.__host_type__.__slots_sort__))
        try:
            csvfilter = kwargs.pop('csvfilter')
        except KeyError:
            csvfilter = None

        self.logger.debug('getting hosts list...')
        _hosts = self.hosts
        if csvfilter:
            self.logger.debug('\t filtering hosts using %s...', csvfilter)
            _hosts = list(filter(lambda h: h.filter(csvfilter, **kwargs), self.hosts))

        self.logger.debug('\t sorting using field [ %s ]...', sort_field)
        return sorted(_hosts, key=lambda _hst: getattr(_hst, sort_field))

    def get_info(self, ipaddress):
        """
        Searches for supplied ipaddress in current inventory hosts
        :param ipaddress: Any ipaddress to look into hosts ip fields interfaces. It doesn't have to be complete,
                          it'll be searched forward from left to right
        :return: Node info if any is found else, a NodeNotFoundError is raised
        """
        try:
            return next(filter(lambda h: ipaddress in [getattr(h, _slt) for _slt in self.__host_type__.__slots_ip__],
                               getattr(self, 'hosts')))
        except StopIteration:
            _logger.debug('\t no host found with ipaddress [ %s ]', ipaddress)
            raise NodeNotFoundError('Could not found node with supplied ipaddress', ipaddress=ipaddress)

    def save(self, **kwargs):
        """
        Persists current inventory to file, or provided inventory dictionary
        :param kwargs: Extra arguments
           filename: Name of the file to save the results into
              idict: Inventory dictionary, if none is provided, then current content is persisted
        """
        idict = kwargs.get('idict', self.get_inventory())
        idict['hosts'] = [h.get_dict() for h in idict['hosts']]

        _filename = kwargs.get('filename', f'{self.__service__}_{self.env.name}_search_{self.date}.json')

        self.logger.info(f'saving inventory to {_filename}...')
        if os.path.isfile(_filename):
            if input_wait(f'overwrite {_filename}?') == 'N':
                return

        with open(_filename, 'w') as _fb:
            _fb.write(json.dumps(idict, indent=4))
            _fb.flush()

    def print(self, **kwargs):
        """
        Outputs inventory to console as formatted text
        :param kwargs:
             idict: If given, then print this inventory dictionary, else, print current inventory dictionary
         csvfilter: A CSV formatted line with key:value pairs to match in inventory. If key:value pairs
                    are found, a dictionary is returned. If only key values are provided (separated by semicolon too),
                    an array is returned, for example:  role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ...
                    Multiple values can be provided for filtering as  key1:value1,value2;key2:value1;key3:value1 ...
              sort: Name of key to sort the inventory, default hostname (Always ascending). If key does not exists
              in inventory, a warning is printed and no kind of sorting is done
           columns: If given, inventory will be filtered again to removed all columns not given in this list.
        :return: Returns final printed dictionary
        """
        _logger.debug('building table with inventory results...')
        idict = self.check_inventory(kwargs.get('idict', self.get_inventory(**kwargs)))

        # get nodes
        date = idict['date']
        env = idict['env']
        hosts = idict['hosts']
        version = idict['version']

        if len(hosts) == 0:
            print(cs('No results found', COLOR_YELLOW))
            return

        # print headers
        print('-' * self.__host_type__.get_headers_total_length(**kwargs))
        print(cs(f'\t Inventory  ', COLOR_BLUE) + cs(version, COLOR_YELLOW) + cs('  from:   ', COLOR_BLUE)
              + cs(env, COLOR_YELLOW) + cs('  on:   ', COLOR_BLUE) + cs(date, COLOR_YELLOW))
        print('-' * self.__host_type__.get_headers_total_length(**kwargs))
        self.__host_type__.print_headers(**kwargs)
        print('-' * self.__host_type__.get_headers_total_length(**kwargs))

        for _hst in hosts:
            _logger.debug('\t processing host [ %s ]', _hst)
            _hst.print(**kwargs)
        print('-' * self.__host_type__.get_headers_total_length(**kwargs))

        return idict

    # todo: add gvp inventory

    @classmethod
    def check_inventory(cls, content):
        """
        Checks if supplied inventory has correct format
        :param content: Inventory as a dictionary
        """
        assert isinstance(content, dict), cs('Inventory must be a dictionary', COLOR_RED)

        _logger.debug('checking inventory schema...')
        with open(get_resource_path('inventory_schema.json')) as _fb:
            _schema = json.loads(_fb.read())

        try:
            # fixme: Solution for those cases where hosts are dict and other times instances of InventoryHost
            # in case supplied inventory has instances of InventoryHost instead of dictionaries as 'hosts'
            if isinstance(content['hosts'][0], InventoryHost):
                _content = content.copy()
                _content['hosts'] = [h.get_dict() for h in content['hosts']]
            else:
                _content = content
        except KeyError:
            raise WrongInventoryException('Missing required argument', arg_name='hosts')

        validate(instance=_content, schema=_schema)

        # check that it's from correct service
        if content['service'] != cls.__service__:
            raise WrongInventoryException('Supplied inventory has wrong service', expected=cls.__service__,
                                          found=content['service'])

        return content

    @classmethod
    def check_environment(cls, env_name):
        """
        Checks supplied inventory name, and provide the correct value from inventory environments attribute
        """
        assert env_name, cs('Supplied env name is None')

        cls.logger.debug('checking supplied environment [ %s ]', env_name)
        for _env in cls.__environments__:
            if env_name == _env.name:
                cls.logger.debug('\t correct')
                return _env
        raise WrongEnvironmentException(env_name)

    @classmethod
    def check_host_valid(cls, host):

        if isinstance(host, InventoryHost):
            return host

        assert isinstance(host, dict), cs('host must be a dictionary with correct invetnory host fields')

        for _key in host.keys():
            assert cls.check_field_valid(_key), 'Host keys must be valid inventory keys'
        return host

    @classmethod
    def new_filter(cls, csv_text):
        """
        Builds an instance of InventoryFilter  with supplied csv formatted string.
        WARN: ONLY valid for String filtering!!
        :param csv_text: String to be used as filter. It's a CSV formatted line with key:value pairs to match in
            inventory. If key:value pairs are found, a dictionary is returned. If only key values are provided
            (separated by semicolon too), an array is returned, for example: field:value;field2:value2...
            or FIELD;FIELD2;FIELD3... field names can be uppercase or lowercase, it doesn't matter
            Multiple values can be provided for filtering as key1:value1,value2;key2:value1,value2...'
        :return: An array or a dictionary  dictionary with generated filtering values
        """
        return cls.__host_type__.new_filter(csv_text)

    @classmethod
    def check_filter(cls, csvfilter):
        return cls.__host_type__.check_filter(csvfilter)

    @classmethod
    def check_version(cls, version):
        """
        Method that checks that version's format is correct
        :param version: version to check
        """
        assert version, cs('No version supplied')
        if version == 'current':
            return version
        elif not cls.VERSION_PATTERN.match(version):
            raise MissingArgumentException('Version format is wrong. Expected: '
                                           '"a.b.c" where a,b and c are integers',
                                           version=version)
        return version

    @abc.abstractmethod
    def build(self, **kwargs):
        """
        Builds inventory from from original source content, or supplied source
        :param kwargs: Extra arguments
            source: Any alternative source to get original content from
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def export(self, **kwargs):
        """
        Transform inventory to different formats
        """
        raise NotImplementedError()

    @classmethod
    def clone_from(cls, _idict):
        """
        Fills instance slots with supplied dictionary inventory
        :param _idict: A dictionary with an inventory
        """
        cls.logger.debug("setting current instance's slots values from supplied dictionary")
        _idict = cls.check_inventory(_idict)

        for _sl in cls.__slots__:
            _value = _idict[_sl]
            if _sl == 'env':
                _value = cls.check_environment(_value)
            elif _sl == 'hosts':
                _value = [cls.__host_type__.of(**d) for d in _value]
            setattr(cls, _sl, _value)


# -- cdn service

class CdnInventoryHost(InventoryHost):
    # inventory service name. This host can only be used in this kind of service
    __service__ = 'cdn'

    # host fields
    __slots__ = ('os', 'hostname', 'fqdn', 'site_id', 'region_name', 'ob', 'country', 'city', 'role',
                 'ipaddress_management', 'ipaddress_service', 'ipaddress_service_iptv')

    # dictionary with len of inventory fields. It'll be used for printing content
    __slots_len__ = {'os': 7, 'hostname': 28, 'fqdn': 35, 'site_id': 30, 'region_name': 14, 'ob': 14,
                     'country': 10, 'city': 30, 'role': 15,
                     'ipaddress_management': 16, 'ipaddress_service': 16, 'ipaddress_service_iptv': 16}

    # list of fields with IP information
    __slots_ip__ = ('ipaddress_management', 'ipaddress_service', 'ipaddress_service_iptv')

    # Default sorting field in inventory
    __slots_sort__ = 'hostname'

    # default slots udnode
    __slots_udnode__ = ('hostname', 'role', 'region_name', 'country', 'city')

    logger = logging.getLogger(f'{__service__}_host')

    # Explanation: udnode roles for proxys
    #
    # Spain cyp*   => proxy live
    # Latam clp*   => proxy live
    # Latam clop*  => proxy VoD
    # Spain cod*   => origin (VoD) origin-proxy
    # Latam clos*  => origin (VoD) origin-proxy
    # exceptions: brasil, there are proxys that are live and VoD
    # No more proxyhybrid exists, moved to VoD
    ROLE_MAP_PROXY = {'cyp': 'proxynodelive', 'clp': 'proxynodelive',
                      'cod': 'proxy', 'clos': 'proxy',
                      'clop': 'proxynodevod'
                      }
    ROLE_MAP = {'origin_cdnnode': 'origin', 'origin_webdav': 'webdav', 'tld_instance': 'tld'}

    def __udnode_role(self):
        """
        Provides a mapping for udnode's role
        """
        _role = getattr(self, 'role')
        if 'proxy' in _role:
            for _key, _value in self.ROLE_MAP_PROXY.items():
                if getattr(self, 'hostname').startswith(_key):
                    return _value
        return self.ROLE_MAP.get(_role, _role)

    def __udnode_region_name(self):
        """
        Provides udnode region_name value
        """
        # region name
        try:
            _region_name = getattr(self, 'ob').split('_IPTV')[0]
        except KeyError:
            _region_name = 'unknown'
        return _region_name

    def udnode(self, **kwargs):
        """
        Writes current host content in udnode format:

            ipaddress_service|HOSTNAME|ROLE|deliveryRegion|Country|City|latitude|longitude

        if service iPTV is defined, then an extra line needs to be added. Since gps data is needed, if none is provided,
        then latitude and longitude will be 0

            ipaddress_service_iptv|HOSTNAME|ROLE|deliveryRegion|Country|City|latitude|longitude

        :param kwargs: Extra args
            location: Gps data information as (latitude, longitude)
        return: A string with current host data in udnode format
        """
        latitude, longitude = kwargs.get('location', (0, 0))

        _service_iptv = getattr(self, 'ipaddress_service_iptv')
        _region_name = self.__udnode_region_name()

        _left = f'{getattr(self, "hostname")}|{self.__udnode_role()}'
        _right = f'{getattr(self, "country")}|{getattr(self, "city")}|{latitude}|{longitude}'

        # fields
        _line = f'{getattr(self, "ipaddress_service")}|{_left}|{_region_name}|{_right}'

        if _service_iptv:
            _line += '\n'
            _line += f'{_service_iptv}|{_left}|{_region_name}_IPTV|{_right}'
        return _line


class CdnInventory(Inventory):
    # inventory service name
    __service__ = 'cdn'

    # Array with InventoryEnvironment instances
    __environments__ = (InventoryEnv('pro',
                                     source='http://cdn-deploy-manager.cdn.hi.inet/cdn/repositories/VERSION/docs/'
                                            'environment/production.yaml',
                                     service='cdn',
                                     local='cdn_pro_VERSION.json',
                                     gps='cdn_pro_gps_VERSION.json'),
                        InventoryEnv('pre',
                                     source='http://cdn-deploy-manager.cdn.hi.inet/cdn/repositories/VERSION/docs/'
                                            'environment/prepro.yaml',
                                     service='cdn',
                                     local='cdn_pre_VERSION.json',
                                     gps='cdn_pre_gps_VERSION.json'),
                        InventoryEnv('opt',
                                     source='http://cdn-deploy-manager.cdn.hi.inet/cdn/repositories/VERSION/docs/'
                                            'environment/opt.yaml',
                                     service='cdn',
                                     local='cdn_opt_VERSION.json',
                                     gps='cdn_opt_gps_VERSION.json')
                        )

    __environment_default__ = 'pro'

    # Host types for current inventory
    __host_type__ = CdnInventoryHost

    __version_required__ = True

    __home_dir__ = __service__

    __expires__ = True

    logger = logging.getLogger(f'{__service__}_inv')

    def build(self, **kwargs):
        _logger.debug('building %s inventory...', self.__service__)

        # check if original source was provided
        try:
            source = kwargs.pop('source')
        except KeyError:
            source = ''

        # load content from original source in environment
        try:
            source = check_path(source, extensions=['yaml'])
            self.logger.info('reading supplied source [ %s ]...', source)
            with open(source) as _fb:
                content = _fb.read()
        except FileNotExistsError:
            source = self.env.get_source(version=self.version)
            self.logger.info('reading original source [ %s ]...', source)
            content = get_httpfile_content(source, progress=True)

        try:
            # if content is yaml, then load it and create our inventory
            _logger.info('\t  building json inventory...')
            pbScheduler = ProgressBarScheduler(f'Building inventory', ratio=4)
            pbScheduler.start()
            content = yaml.load(content, Loader=yaml.CLoader)

            # todo: refactor so final class instantiation is not done in build, but in final target method
            self.hosts = [CdnInventoryHost.of(**{'os': CdnInventoryHost.KEY_LINUX,
                                                 'fqdn': nd['facts']['fqdn'],
                                                 'hostname': nd['facts']['hostname'],
                                                 'site_id': nd['facts']['site_id'],
                                                 'region_name': nd['facts']['region_name'],
                                                 'ob': nd['facts']['ob'],
                                                 'country': nd['facts']['country'],
                                                 'city': nd['facts']['city'],
                                                 'role': nd['facts']['role'],
                                                 'ipaddress_management': nd['facts']['ipaddress_management'],
                                                 'ipaddress_service': nd['facts']['ipaddress_service'],
                                                 'ipaddress_service_iptv': nd['facts'].get('ipaddress_service_iptv', "")
                                                 })
                          for nd in content['hosts']]
        except KeyError as ex:
            raise CouldNotBuildInventoryException('could not build inventory') from ex
        finally:
            pbScheduler.quit()

        # save inventory
        self.save(filename=self.env.get_local(version=self.version, nocheck=True))

    def __export_udnodes(self, idict, **kwargs):
        """
        Exports inventory to udnode format
        :param idict: Inventory as dictionary to export
        :param kwargs: Extra arguments
             filename: Output filename instead of default one
        """
        # gps inventory
        _inv_gps = CdnGpsInventory('pro', version=getattr(self, 'version'))
        _inv_gps.load(source=kwargs.get('source'))

        self.logger.info('exporting inventory to udnodes...')
        _filename = kwargs.get('filename', f'udnodes_{self.__service__}_{self.env.name}_{self.date}.csv')
        with open(_filename, 'w') as _fb:
            for _ihst in idict['hosts']:
                try:
                    _ghst = next(filter(lambda host: host.hostname == _ihst.hostname, _inv_gps.hosts))
                    _line = _ihst.udnode(location=(_ghst.latitude, _ghst.longitude))
                    _fb.write(f'{_line}\n')
                except StopIteration:
                    self.logger.error('host [ %s ] not found in gps inventory', _ihst.hostname)
                    continue
        return idict

    def __export_st2(self, idict, **kwargs):
        """
        Exports inventory to st2's json batch schema
        :param idict: Inventory as dictionary to export
        :param kwargs: Extra arguments
             username: If supplied, this username is used instead of default
             password: If supplied, this password will be used for authentication in all hosts
              keyfile: If supplied, this Keyfile will be used in authentication for all hosts
                 port: Port to be used instead of default one
              timeout: Timeout in seconds for connections, instead of default ones
             filename: Output filename instead of default one
             commands: A json expression with an array of commands, as:
                       {"commands":[{"name":"name1", "action":"action1"}, {"name":"name2", "action":"action2"},...]}
        """
        self.logger.info('exporting inventory to st2 batch schema...')
        _filename = kwargs.get('filename', f'st2batch_{self.__service__}_{self.env.name}_{self.date}.json')

        # commands
        _commands = kwargs.get(RemoteExecutor.FIELDS.COMMANDS, [])
        if not _commands:
            for _key in ('status_zabbix', 'status_telegraf', 'status_tdagent'):
                _commands.append({CONFIG_FIELDS.NAME: ST2_PRO_COMMANDS[_key][CONFIG_FIELDS.NAME],
                                  CONFIG_FIELDS.ACTION: ST2_PRO_COMMANDS[_key][CONFIG_FIELDS.SSH]})

        _st2hosts = []
        for _hst in idict['hosts']:
            _shst = dict()
            _shst[RemoteExecutor.FIELDS.IP] = _hst.ipaddress_management
            _shst[RemoteExecutor.FIELDS.HOSTNAME] = _hst.hostname
            _shst[RemoteExecutor.FIELDS.PORT] = kwargs.get(RemoteExecutor.FIELDS.PORT, DEFAULT_SSH_PORT)
            _shst[RemoteExecutor.FIELDS.TIMEOUT] = kwargs.get(RemoteExecutor.FIELDS.TIMEOUT, 5)
            _shst[RemoteExecutor.FIELDS.OS] = _hst.os
            _shst[RemoteExecutor.FIELDS.AUTHS] = [ST2_PRO_AUTHS[CONFIG_FIELDS.SSH]]
            _shst[RemoteExecutor.FIELDS.COMMANDS] = _commands
            _st2hosts.append(_shst)

        # replace hosts in inventory`
        idict['hosts'] = _st2hosts

        # fixme: Refactor input_wait to allow for timeout termination. Usefull in unattended operations
        self.logger.info('saving batch file %s...', _filename)
        if os.path.isfile(_filename):
            input_wait(f'{_filename} exists, overwrite?')
        with open(_filename, 'w') as _fb:
            _fb.write(json.dumps(idict, indent=4))

    def export(self, **kwargs):
        """
        Exports supplied inventory to other formats
        :param kwargs: Extra args
             idict: Inventory as a dictionary (where hosts ar instances of CdnInventoryHost)
         csvfilter: A CSV formatted line with key:value pairs to match in inventory. If key:value pairs
                    are found, a dictionary is returned. If only key values are provided (separated by semicolon too),
                    an array is returned, for example:  role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ...
                    Multiple values can be provided for filtering as  key1:value1,value2;key2:value1;key3:value1 ...
              sort: Name of key to sort the inventory, default hostname (Always ascending). If key does not exists
                    in inventory, a warning is printed and no kind of sorting is done
           udnodes: Create udnodes formatted file from inventory
               st2: Creates a batch file that complies batch_schema.json, with result from searched inventory. It uses
                    username password and keyfile from config's file st2 section, but if any of these args are supplied
                    in kwargs, then these are the ones used overriding appconfig values.
          filename: Output filename instead of default one
        """
        _logger.debug('exporting inventory results to other format...')
        _idict = self.check_inventory(kwargs.get('idict', self.get_inventory(**kwargs)))

        if kwargs.get('udnodes'):
            return self.__export_udnodes(_idict, **kwargs)
        elif kwargs.get('st2'):
            return self.__export_st2(_idict, **kwargs)


class CdnGpsInventoryHost(InventoryHost):
    """
    Class that encapsulates the gps data of host inventory
    """

    # inventory service name. This host can only be used in this kind of service
    __service__ = 'cdn_gps'

    # host fields
    __slots__ = ('hostname', 'country', 'city', 'ipaddress_service', 'latitude', 'longitude')

    # dictionary with len of inventory fields. It'll be used for printing content
    __slots_len__ = {'hostname': 28, 'country': 10, 'city': 30, 'ipaddress_service': 16, 'latitude': 6, 'longitude': 6}

    # gps data fields
    __slots__gps__ = ('latitude', 'longitude')

    # fields with IP information
    __slots_ip__ = ('ipaddress_service',)

    # Default sorting field in inventory
    __slots_sort__ = 'hostname'

    logger = logging.getLogger(f'{__service__}_host')


class CdnGpsInventory(Inventory):
    """
    Hosts inventory with GPS data
    """
    # inventory service name
    __service__ = 'cdn_gps'

    # Array with InventoryEnvironment instances
    __environments__ = (InventoryEnv('pro',
                                     source='cdn_pro_VERSION.json',
                                     service='cdn_gps',
                                     home='cdn',
                                     local='cdn_gps_pro_VERSION.json'),
                        InventoryEnv('pre',
                                     source='cdn_pre_VERSION.json',
                                     service='cdn_gps',
                                     home='cdn',
                                     local='cdn_gps_pre_VERSION.json'),
                        InventoryEnv('opt',
                                     source='cdn_opt_VERSION.json',
                                     service='cdn_gps',
                                     home='cdn',
                                     local='cdn_gps_opt_VERSION.json')
                        )

    __environment_default__ = 'pro'

    # Host types for current inventory
    __host_type__ = CdnGpsInventoryHost

    __version_required__ = True

    __expires__ = False

    logger = logging.getLogger(f'{__service__}_inv')

    def build(self, **kwargs):
        _logger.debug('building %s inventory...', self.__service__)

        # check if original source was provided
        try:
            source = kwargs.pop('source')
        except KeyError:
            source = ''

        # load content from original source in environment
        try:
            source = check_path(source, extensions=['json'])
            self.logger.debug('reading supplied source [ %s ]...', source)
        except FileNotExistsError:
            source = self.env.get_source(version=self.version)
            self.logger.debug('reading original source [ %s ]...', source)

        try:
            # read content
            with open(source) as _fb:
                content = json.loads(_fb.read())

            # build gps inventory
            if input_wait('Gps data generation can take 2/3 min, proceed?') == 'N':
                return

            self.logger.info('building gps data...')
            pbar = tqdm(total=len(content['hosts']), desc='Nodes', position=0, colour='blue')
            for nd in content['hosts']:
                _hst = CdnGpsInventoryHost.of(**{'hostname': nd['hostname'],
                                                 'country': nd['country'],
                                                 'city': nd['city'],
                                                 'ipaddress_service': nd['ipaddress_service'],
                                                 'latitude': '',
                                                 'longitude': ''
                                                 })
                # update gps data information
                try:
                    location = get_ip_location(nd['ipaddress_service'])
                except CouldNotGetIpInfoException:
                    self.logger.info('\t\t could not get ip information for [ %s ][ %s ]',
                                     nd['hostname'], nd['ipaddress_service'])
                    location = '0,0'
                finally:
                    _logger.debug('\t adding location info [ %s ]', location)
                    location = location.split(',')
                    setattr(_hst, 'latitude', location[0])
                    setattr(_hst, 'longitude', location[1])
                    pbar.update(1)

                self.logger.debug('\t new host added %s', _hst)
                self.hosts.append(_hst)
            pbar.close()

            self.save(filename=self.env.get_local(version=self.version, nocheck=True))

        except (KeyError, TypeError) as ex:
            raise CouldNotBuildInventoryException('could not build inventory') from ex

    def export(self, **kwargs):
        pass


# -- gvp service

class GvpInventoryHost(InventoryHost):
    __service__ = 'gvp'

    __slots__ = ('os', 'hostname', 'fqdn', 'ipaddress_management')

    # dictionary with len of inventory fields. It'll be used for printing content
    __slots_len__ = {'os': 7, 'hostname': 28, 'fqdn': 35, 'ipaddress_management': 16}

    # list of fields with IP information
    __slots_ip__ = ('ipaddress_management',)

    # Default sorting field in inventory
    __slots_sort__ = 'hostname'

    __slots_orig__ = ('hostname', 'fqdn', 'os', 'ipaddress_management')

    logger = logging.getLogger(f'{__service__}_host')


class GvpInventory(Inventory):
    __service__ = 'gvp'

    # Array with InventoryEnvironment instances
    __environments__ = (InventoryEnv('pro',
                                     source='gvp_penuelas.csv',
                                     service='gvp',
                                     local='gvp_pro.json'),
                        )

    __environment_default__ = 'pro'

    __host_type__ = GvpInventoryHost

    __version_required__ = False

    __home_dir__ = __service__

    __expires__ = False

    logger = logging.getLogger(f'{__service__}_inv')

    def _get_args_from_csv(self, csvline):
        """
        Provides a dictionary with node information from supplied csv formatted line
        :param csvline: CSV formatted line with node information
        :return: A dict with node information
        """
        assert csvline and isinstance(csvline, str), cs('csvline must be a csv formatted string', COLOR_RED)

        csvline = csvline.strip().split(',')
        _dict = {self.__host_type__.__slots_orig__[index]: csvline[index] for index in
                 range(len(self.__host_type__.__slots_orig__))}

        # process hostname
        _dict['hostname'] = _dict['hostname'].split('.')[0]

        # process os
        _os_lower = _dict['os'].lower()
        if InventoryHost.KEY_WINDOWS in _os_lower:
            _dict['os'] = InventoryHost.KEY_WINDOWS
        else:
            _dict['os'] = InventoryHost.KEY_LINUX

        # -- process ip
        if '"' in _dict['ipaddress_management']:
            try:
                _ip = next(filter(lambda ip: ip != '', [ip.strip() for ip in _dict['ipaddress_management']
                                  .strip('[').strip(']').replace("'", "").split(',')]))
            except StopIteration:
                _ip = ""
            _dict['ipaddress_management'] = _ip
        _logger.debug('new gvp dict from csv line %s', _dict)
        return _dict

    def build(self, **kwargs):
        _logger.debug('building %s inventory...', self.__service__)

        # check if original source was provided
        try:
            source = kwargs.pop('source')
        except KeyError:
            source = ''

        # load content from original source in environment
        try:
            source = check_path(source, extensions=['csv'])
            self.logger.info('reading supplied source [ %s ]...', source)
        except FileNotExistsError:
            source = self.env.get_source(version=self.version)
            self.logger.info('reading original source [ %s ]...', source)

        # read content from source
        with open(source) as _fb:
            content = _fb.readlines()

        try:
            # process csv content and create our inventory
            _logger.info('\t  building json inventory...')
            pbar = ProgressBar(total=len(content), desc='Lines', position=0, colour='blue', fake=False)
            for _csvline in content:
                _lower = _csvline.lower()
                if self.__host_type__.KEY_LINUX not in _lower and self.__host_type__.KEY_WINDOWS not in _lower:
                    _logger.debug('\t skipping node, not windows or linux')
                    pbar.update(1)
                    continue
                self.hosts.append(GvpInventoryHost.of(**self._get_args_from_csv(_csvline)))
                pbar.update(1)
        except KeyError as ex:
            raise CouldNotBuildInventoryException('could not build inventory') from ex
        finally:
            pbar.close()

        # save inventory
        self.save(filename=self.env.get_local(version=self.version, nocheck=True))

    def __export_st2(self, idict, **kwargs):
        """
        Exports inventory to st2's json batch schema
        :param idict: Inventory as dictionary to export
        :param kwargs: Extra arguments
             username: If supplied, this username is used instead of default
             password: If supplied, this password will be used for authentication in all hosts
              keyfile: If supplied, this Keyfile will be used in authentication for all hosts
                 port: Port to be used instead of default one
              timeout: Timeout in seconds for connections, instead of default ones
             filename: Output filename instead of default one
             commands: A json expression with an array of commands, as:
                       {"commands":[{"name":"name1", "action":"action1"}, {"name":"name2", "action":"action2"},...]}
        """
        self.logger.info('exporting inventory to st2 batch schema...')
        _filename = kwargs.get('filename', f'st2batch_{self.__service__}_{self.env.name}_{self.date}.json')

        # commands
        _commands = kwargs.get(RemoteExecutor.FIELDS.COMMANDS, [])

        _st2hosts = []
        for _hst in idict['hosts']:
            _shst = dict()
            _shst[RemoteExecutor.FIELDS.IP] = _hst.ipaddress_management
            _shst[RemoteExecutor.FIELDS.HOSTNAME] = _hst.hostname
            _shst[RemoteExecutor.FIELDS.PORT] = kwargs.get(RemoteExecutor.FIELDS.PORT, DEFAULT_SSH_PORT)
            _shst[RemoteExecutor.FIELDS.TIMEOUT] = kwargs.get(RemoteExecutor.FIELDS.TIMEOUT, 5)
            _shst[RemoteExecutor.FIELDS.OS] = _hst.os
            _shst[RemoteExecutor.FIELDS.AUTHS] = [ST2_PRO_AUTHS[CONFIG_FIELDS.SSH], ST2_PRO_AUTHS[CONFIG_FIELDS.BASIC]]

            if _hst.os == InventoryHost.KEY_WINDOWS:
                _action_type = CONFIG_FIELDS.WINRM
            else:
                _action_type = CONFIG_FIELDS.SSH

            if not _commands:
                _commands = [{CONFIG_FIELDS.NAME: ST2_PRO_COMMANDS[_key][CONFIG_FIELDS.NAME],
                              CONFIG_FIELDS.ACTION: ST2_PRO_COMMANDS[_key][_action_type]} for
                             _key in ('status_zabbix', 'status_telegraf', 'status_tdagent')]

            _shst[RemoteExecutor.FIELDS.COMMANDS] = _commands
            _st2hosts.append(_shst)

        # replace hosts in inventory`
        idict['hosts'] = _st2hosts

        # fixme: Refactor input_wait to allow for timeout termination. Usefull in unattended operations
        self.logger.info('saving batch file %s...', _filename)
        if os.path.isfile(_filename):
            input_wait(f'{_filename} exists, overwrite?')
        with open(_filename, 'w') as _fb:
            _fb.write(json.dumps(idict, indent=4))

    def export(self, **kwargs):
        """
        Exports supplied inventory to other formats
        :param kwargs: Extra args
             idict: Inventory as a dictionary (where hosts ar instances of CdnInventoryHost)
         csvfilter: A CSV formatted line with key:value pairs to match in inventory. If key:value pairs
                    are found, a dictionary is returned. If only key values are provided (separated by semicolon too),
                    an array is returned, for example:  role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ...
                    Multiple values can be provided for filtering as  key1:value1,value2;key2:value1;key3:value1 ...
              sort: Name of key to sort the inventory, default hostname (Always ascending). If key does not exists
                    in inventory, a warning is printed and no kind of sorting is done
               st2: Creates a batch file that complies batch_schema.json, with result from searched inventory. It uses
                    username password and keyfile from config's file st2 section, but if any of these args are supplied
                    in kwargs, then these are the ones used overriding appconfig values.
          filename: Output filename instead of default one
        """
        _logger.debug('exporting inventory results to other format...')
        _idict = self.check_inventory(kwargs.get('idict', self.get_inventory(**kwargs)))

        if kwargs.get('st2'):
            return self.__export_st2(_idict, **kwargs)


# -- buckets

class BucketEnvironment:
    """
    Class that contains logic about certain bucket environment
    """

    def __init__(self, source, local):
        """
        :param source: Source location of inventory content
        :param local: Inventory content location
        """
        self.source = source
        self.local = local


class InventoryFactory:
    SERVICES = {'cdn': CdnInventory, 'gvp': GvpInventory}

    @staticmethod
    def check_service(name):
        if name not in InventoryFactory.SERVICES.keys():
            raise MissingArgumentException('Supplied service not supported', supplied=name, allowed=Inventory.SERVICES)

    @classmethod
    def get_type(cls, name):
        InventoryFactory.check_service(name)
        return InventoryFactory.SERVICES[name]

    @staticmethod
    def of(name, **kwargs):
        return InventoryFactory.get_type(name)(kwargs.pop('env'), **kwargs)
