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
    def do_all(self, line):
        """all: Prints all string representation of all instances or
        not on class name
        usage: all
        or usage: all class_name
        """
        str_list_cls_name = []
        dict_objects = storage.all()
        if line:
            if line in HBNBCommand.class_names_list:
                for key, obj in dict_objects.items():
                    cls_name = key.split(".")[0]
                    if cls_name in HBNBCommand.class_names_list:
                        str_list_cls_name.append(str(obj))
                print(str_list_cls_name)
            else:
                print("** class doesn't exist **")
        else:
            for key, obj in dict_objects.items():
                cls_name = key.split(".")[0]
                if cls_name in HBNBCommand.class_names_list:
                    str_list_cls_name.append(str(obj))
            print(str_list_cls_name)

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

    def do_destroy(self, line):
        """detroy: Deletes and instance based on a class name and id
        usage: destroy class_name id
        """
        if line:
            class_name = line.split(" ")[0]
            if class_name in HBNBCommand.class_names_list:
                length = len(line.split(" "))
                if length >= 2:
                    match = False
                    dictionary = storage.all()
                    id = line.split(" ")[1]
                    for key, value in dictionary.items():
                        id_key = key.split(".")[1]
                        if id == id_key:
                            match = True
                            key = key
                            break
                    if match:
                        dictionary.pop(key)
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")

            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

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
                    dictionary = storage.all()
                    for key, value in dictionary.items():
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
