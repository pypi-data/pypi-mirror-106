"""
Module with logic to create, edit and convert inventory files
"""
import getpass
import logging

from stringcolor import cs

from videotools import COLOR_BLUE
from videotools.inventory import NodeNotFoundError, Inventory, InventoryFactory
from videotools.net import DEFAULT_SSH_PORT, DEFAULT_TIMEOUT

_logger = logging.getLogger('inv_cmd')


# -- methods


def _search_inventory(service, **kwargs):
    """
    Searches into a given inventory with supplied filter values,a nd always provides Management and Service IP addresses
    :param service: Name of the inventory service: cdn, gvp (default: cdn)
    :param kwargs: Any extra arguments
              env: Name of the environment for the inventory or file to search into
        csvfilter: A CSV formatted line with key:value pairs to match in inventory. If key:value pairs
                   are found, a dictionary is returned. If only key values are provided (separated by semicolon too),
                   an array is returned, for example:  role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ...
                   Multiple values can be provided for filtering as  key1:value1,value2;key2:value1;key3:value1 ...
          columns: If given, inventory will be filtered again to removed all columns not given in this list. Powerful
                    when combined with csvfilter
           source: If given, inventory will be loaded from this source
             case: If given, inventory will be filtered using case sensitive matching
             sort: If given, inventory will be sorted ascending by given column name
             json: If given, search results will be save in a json file
          udnodes: If given, a new file with ud_nodes format is generated with inventory fields:
                       Service IP|HOSTNAME|ROLE|deliveryRegion|Country|latitude|longitud
                   from supplied environment
    :return: Prints search results, and persists them if json argument is given. If conversion options are supplied,
             other file formats are generated too
    """
    # load and print inventory
    _logger.info('searching hosts...')
    inv = InventoryFactory.of(service, **kwargs)
    inv.load(**kwargs)

    if kwargs.get('udnodes'):
        _idict = inv.export(**kwargs)
    else:
        _idict = inv.print(**kwargs)

    if kwargs.get('json', False):
        inv.save(idict=_idict)


# todo: search in all inventories, not only in the one that matches supplied service name
def _show_info(service, ipaddress, **kwargs):
    """
    Shows node information, if found, with given data. Current implementation searches in the ip fields of hosts
    :param service: Name of the inventory service: cdn, gvp (default: cdn)
    :param ipaddress: Any ipaddress to look into ip fields of hosts in inventory
    :param kwargs: Any extra arguments
            env: Name of the environment for the inventory or file to search into
         source: If given, inventory will be loaded from this source
    :return: Node information
    """
    _logger.info('searching for node with ipaddress [ %s ] ...', ipaddress)

    inv = InventoryFactory.of(service, **kwargs)
    inv.load(source=kwargs.get('source'))

    try:
        node = inv.get_info(ipaddress)
        node.print(info=ipaddress)
    except NodeNotFoundError:
        print(cs('No results found', COLOR_BLUE))


def _st2_batch(service, **kwargs):
    """
    Creates a batch file that complies batch_schema.json, with result from searched inventory. It uses username
    password and keyfile from config's file st2 section, but if any of these args are supplied in kwargs, then these
    are the ones used overriding appconfig values.
    :param service: Name of the inventory service: cdn, gvp (default: cdn)
    :param kwargs: Any extra arguments
                env: Name of the environment for the inventory or file to search into
        csvfilter: A CSV formatted line with key:value pairs to match in inventory. If key:value pairs
                   are found, a dictionary is returned. If only key values are provided (separated by semicolon too),
                   an array is returned, for example:  role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ...
                   Multiple values can be provided for filtering as  key1:value1,value2;key2:value1;key3:value1 ...
           source: If given, inventory will be loaded from this source
             case: If given, inventory will be filtered using case sensitive matching
             sort: If given, inventory will be sorted ascending by given column name
         username: If supplied, this username is used instead of default
         password: If supplied, this password will be used for authentication in all hosts
          keyfile: If supplied, this Keyfile will be used in authentication for all hosts
             port: Port to be used instead of default one
          timeout: Timeout in seconds for connections, instead of default ones
         commands: A json expression with an array of commands, as:
                   {"commands":[{"name":"name1", "action":"action1"}, {"name":"name2", "action":"action2"},...]}
    :return: Creates a json batch file with results of a search, to be used as input in batch operations from a
             st2 host
    """
    # load and print inventory
    _logger.info('creating st2 batch file...')

    inv = InventoryFactory.of(service, **kwargs)
    inv.load(source=kwargs.get('source'))
    inv.export(st2=True, **kwargs)


def init_parser(parent_parser):
    inv_parser = parent_parser.add_parser('inv', help='Used to manipulate node inventories')
    common_grp = inv_parser.add_argument_group('Common')
    common_grp.add_argument('--service', required=False, help='Name of the inventory service: cdn, gvp (default: cdn)',
                            default='cdn')
    common_grp.add_argument('--env', required=False, help='Name of the environment for the inventory: pro, pre, opt',
                            default='pro')
    common_grp.add_argument('--version', type=lambda v: Inventory.check_version(version=v),
                            help='Use this inventory version when loading inventory files. (Default latest CDN)',
                            required=False, default='current')

    common_grp.add_argument('--source', required=False, help='If given, inventory will be loaded from this source',
                            default=None)

    common_args, _ = inv_parser.parse_known_args()
    inventory_type = InventoryFactory.get_type(common_args.service)

    # -- subparsers
    inv_subparsers = inv_parser.add_subparsers()
    inv_subparsers.required = True

    # -- new inventory
    inv_search = inv_subparsers.add_parser('find', help='Search given inventory file')
    inv_search.set_defaults(func=_search_inventory)
    inv_search_filter = inv_search.add_argument_group('Filtering')
    inv_search_filter.add_argument('csvfilter', nargs='?',
                                   type=lambda csvfilter: inventory_type.new_filter(csvfilter),
                                   help='A CSV formatted line with key:value pairs to match in inventory. If key:value '
                                        'pairs are found, a dictionary is returned. If only key values are provided '
                                        '(separated by semicolon too), an array is returned, for example: '
                                        'role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ... Multiple values can '
                                        'be provided for filtering as key1:value1,value2;key2:value1;key3:value1...',
                                   default=None)
    inv_search_filter.add_argument('--columns', required=False, help='If given, inventory will be filtered again '
                                                                     'to removed all columns not given in this list. '
                                                                     'Powerful when combined with csvfilter',
                                   type=lambda columns: inventory_type.new_filter(columns), default='hostname')
    inv_search_filter.add_argument('--case', required=False, action='store_true',
                                   help='If given, inventory will be filtered using case sensitive matching',
                                   default=False)
    inv_search_filter.add_argument('--sort', required=False,
                                   help='If given, inventory will be sorted ascending by given '
                                        'column name, if exists', default='hostname')

    inv_search_save = inv_search.add_argument_group('Export')
    inv_search_save.add_argument('--json', required=False, action='store_true',
                                 help='If given, inventory will be save in a json file', default=False)
    inv_search_save.add_argument('--udnodes', required=False, action='store_true',
                                 help='If given, a new file with ud_nodes format is generated with inventory fields: '
                                      'Service IP|HOSTNAME|ROLE|deliveryRegion|Country|latitude|longitud from supplied '
                                      'environment. Gps data file must exists, either supplied with '
                                      '--gpsdata option (IN PROGRESS), or from default environment location\n'
                                      'WARN: ONLY VALID FOR CDN',
                                 default=False)
    # cmd_search.add_argument('--gpsdata', required=False, help='If given, this file will be used to get location '
    #                                                           'information, instead of default one, which may be '
    #                                                           'created if does not exists',
    #                         type=lambda _filepath: cdn_plat.check_gpsdata_file(_filepath, load=True), default=None)

    # convert content to another formats or file types
    inv_info = inv_subparsers.add_parser('info', help='Prints a specific node information based on supplied ipaddress')
    inv_info.set_defaults(func=_show_info)
    inv_info.add_argument('ipaddress', nargs='?', help='Any ipaddress of the node, management, service or iptv',
                          type=str, default=None)

    # create a batch file with content
    inv_st2 = inv_subparsers.add_parser('st2', help='Uses inventory content to create a st2 batch file')
    inv_st2.set_defaults(func=_st2_batch)
    inv_st2_filter = inv_st2.add_argument_group('Filtering')
    inv_st2_filter.add_argument('csvfilter', nargs='?',
                                type=lambda csvfilter: inventory_type.new_filter(csvfilter),
                                help='A CSV formatted line with key:value pairs to match in inventory. If key:value '
                                     'pairs are found, a dictionary is returned. If only key values are provided '
                                     '(separated by semicolon too), an array is returned, for example: '
                                     'role:endpoint;site_id:Madrid... or ROLE;CITY;HOSTNAME ... Multiple values can '
                                     'be provided for filtering as key1:value1,value2;key2:value1;key3:value1...',
                                default=None)
    inv_st2_filter.add_argument('--case', required=False, action='store_true',
                                help='If given, inventory will be filtered using case sensitive matching',
                                default=False)
    inv_st2_filter.add_argument('--sort', required=False, help='If given, inventory will be sorted ascending by given '
                                                               'column name, if exists', default='hostname')

    inv_st2_auth = inv_st2.add_argument_group('Auth')
    inv_st2_auth.add_argument('--username', required=False, default=getpass.getuser(),
                              help='If supplied, this username is used instead of default')
    exclusive = inv_st2_auth.add_mutually_exclusive_group()
    exclusive.add_argument('--password', help='Password to use for authentication in all hosts', required=False,
                           default=None)
    exclusive.add_argument('--keyfile', help='Keyfile to use in authentication for all hosts', required=False,
                           default=None)

    inv_st2_net = inv_st2.add_argument_group('Remote')
    inv_st2_net.add_argument('--port', required=False, type=lambda x: x.isnumeric(), default=DEFAULT_SSH_PORT,
                             help='Port to be used instead of default one')
    inv_st2_net.add_argument('--timeout', required=False, type=lambda x: x.isnumeric(), default=DEFAULT_TIMEOUT,
                             help='Timeout in seconds for connections, instead of default ones')
    inv_st2_net.add_argument('--commands', required=False, help='A json expression with an array of commands, as:'
                                                                '{"commands":[{"name":"name1", "action":"action1"},'
                                                                '{"name":"name2", "action":"action2"},...]',
                             default=[])
    return inv_parser


def command(args):
    """
    Process the call in a script with supplied args
    """
    # copy of arguments for function
    cmd_args = vars(args).copy()

    # remove function from copied args
    cmd_args.pop('func')

    # execute func and print output if str or int
    args.func(**cmd_args)
