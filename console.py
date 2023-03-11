#!/usr/bin/python3
"""Console Module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console Class"""

    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit: command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF: Ctrl-D working to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
