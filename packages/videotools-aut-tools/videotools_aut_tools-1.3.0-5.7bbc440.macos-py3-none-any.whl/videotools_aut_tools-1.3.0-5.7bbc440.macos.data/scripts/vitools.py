#!python
"""
Script used as main cli executable to perform operations by Video Tools team
"""
import logging
import sys

__author__ = 'agustin.escamezchimeno@telefonica.com'

from videotools.parsers import cipher, git, net, inventory, CommandParser
from videotools.settings import get_common_parser

class VitoolsScript:

    def __init__(self, sys_args):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.script_args = self.__build_args(sys_args)

    def __build_args(self, sys_args):
        parser = None
        try:
            # build parser
            parser = VitoolsScript.init_parser()

            # let's check supplied params
            self.logger.debug('-----------------------------')
            self.logger.debug('\t Parsing sys arguments...  ')

            script_args = parser.parse_args(sys_args[1:])

            self.logger.debug('\t Argument PARSED [%s]', script_args)

            self.logger.debug('-----------------------------')
            return script_args
        except Exception:
            self.logger.error('\t\t Error verifying arguments')
            if '-h' not in sys_args:
                parser.print_help()
            sys.exit(-1)

    @staticmethod
    def init_parser():
        parser = get_common_parser()
        subparsers = parser.add_subparsers(dest='command')
        subparsers.required = True

        # add cipher command opts
        cipher.init_parser(subparsers)
        git.init_parser(subparsers)
        net.init_parser(subparsers)
        inventory.init_parser(subparsers)

        return parser

    def run(self):
        CommandParser.of(self.script_args.command).module.command(self.script_args)


def init():
    """
    Initialization method added to be able to tests correct script invocation
    :return: Whatever exit from run method
    """
    if __name__ == "__main__":
        script = VitoolsScript(sys.argv)
        sys.exit(script.run())


init()
