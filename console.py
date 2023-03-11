#!/usr/bin/python3
"""Console Module"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Console Class"""

    prompt = "(hbnb)"

    def do_create(self, classname):
        """create: creates a new instance of the BaseModel,
        save it to JSON file and prints the id
        usage: create class_name
        """
        class_names_list = ["BaseModel"]
        if classname:
            if classname in class_names_list:
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name is missing **")

    def do_quit(self, line):
        """Quit: command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF: Ctrl-D working to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
