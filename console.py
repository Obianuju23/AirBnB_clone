#!/usr/bin/python3
"""
This is the console model
it provides the entry to the console with
some specific implementations
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """provides the entry point to the imterpreter"""

    prompt = "(hbnb) "

    def do_quit(self, s):
        """this implements the quit"""
        return True

    def do_EOF(self, s):
        """this implements the EOF"""
        print()
        return True

    def help_quit(self):
        """the implements the help for quit"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """this implements the help for EOF"""
        print("EOF command to exit the program\n")

    def emptyline(self):
        """this overrides the empty line default method"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
