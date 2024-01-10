#!/usr/bin/python3
"""
    The hbnb console
    Console module for the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Returns empty when there's no input
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
