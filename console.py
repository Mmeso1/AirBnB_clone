#!/usr/bin/python3
"""
    The hbnb console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """ class of the command line processor for the hbnb """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
