# -- parsers

class CommandParser:
    # -- list of parser modules
    from videotools.parsers import inventory, cipher, git, net
    VALUES = {'cipher': cipher, 'git': git, 'net': net, 'inv': inventory}

    def __init__(self, name, module):
        self.name = name
        self.module = module

    @staticmethod
    def of(name):
        return CommandParser(name, CommandParser.VALUES[name])


