#!/usr/bin/python3
"""Console Module"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Console Class"""

    prompt = "(hbnb)"
    class_names_list = ["BaseModel"]

    # general purpose methods of the program
    def do_create(self, classname):
        """create: creates a new instance of the BaseModel,
        save it to JSON file and prints the id
        usage: create class_name"""
        if classname:
            if classname in HBNBCommand.class_names_list:
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name is missing **")

    def do_show(self, line):
        """show: prints the string representation of a instance based on
        the class name and id.
        usage: show class_name id
        """
        if line:
            class_name = line.split(" ")[0]
            if class_name in HBNBCommand.class_names_list:
                if len(line.split(" ")) >= 2:
                    match = False
                    id = line.split(" ")[1]
                    dict = storage.all()
                    for key, value in dict.items():
                        id_key = key.split(".")[1]
                        if id == id_key:
                            match = True
                            obj = value
                            break
                    if match:
                        print(obj)
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    # methods to exit the program
    def do_quit(self, line):
        """Quit: command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF: Ctrl-D working to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
