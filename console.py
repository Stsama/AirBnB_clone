#!/usr/bin/python3
"""Defines the HBnB console."""


import cmd
class HBNBCommand(cmd.Cmd):
    """Represents a command class"""

    prompt = "(hbnb)"
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True
    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
