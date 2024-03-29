#!/usr/bin/python3
"""Console Module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Console Class"""

    prompt = "(hbnb)"
    class_names_list = ["BaseModel", "User", "Place", "State", "City",
                        "Amenity", "Review"]

    def do_create(self, classname):
        """create: creates a new instance of the BaseModel,
        save it to JSON file and prints the id
        usage: create class_name"""
        if classname:
            if classname in HBNBCommand.class_names_list:
                if classname == "BaseModel":
                    new_model = BaseModel()
                elif classname == "User":
                    new_model = User()
                elif classname == "State":
                    new_model = State()
                elif classname == "City":
                    new_model = City()
                elif classname == "Place":
                    new_model = Place()
                elif classname == "State":
                    new_model = State()
                elif classname == "City":
                    new_model = City()
                elif classname == "Amenity":
                    new_model = Amenity()
                elif classname == "Review":
                    new_model = Review()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show: prints the string representation of a instance based on
        the class name and id.
        usage: show class_name id
        """
        args = line.split()
        if line:
            if args[0] not in HBNBCommand.class_names_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            # class name exists and id also exits
            else:
                class_name = args[0]
                id = args[1]
                found = False
                key_id = class_name + "." + id
                obj_dict = storage.all()
                for key, value in obj_dict.items():
                    if key_id == key:
                        found = True
                        print(value)
                        break
                if not found:
                    print("** no instance found **")
        else:
            print("** class name missing **")
        # if line:
        #    class_name = line.split(" ")[0]
        #    if class_name in HBNBCommand.class_names_list:
        #        if len(line.split(" ")) >= 2:
        #            match = False
        #            id = line.split(" ")[1]
        #            # print(id)
        #            dictionary = storage.all()
        #            for key, value in dictionary.items():
        #                id_key = key.split(".")[1]
        #                if id == id_key:
        #                    match = True
        #                   break
        #            if match:
        #                print(obj)
        #            else:
        #                print("** no instance found **")
        #        else:
        #            print("** instance id missing **")
        #    else:
        #        print("** class doesn't exist **")
        # else:
        #    print("** class name missing **")

    def do_destroy(self, line):
        """detroy: Deletes and instance based on a class name and id
        usage: destroy class_name id
        """
        args = line.split()

        if line:
            if args[0] not in HBNBCommand.class_names_list:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                found = False
                class_name = args[0]
                id = args[1]
                name_id_key = class_name + "." + id
                obj_dict = storage.all()
                for key, value in obj_dict.items():
                    if name_id_key == key:
                        print(value)
                        found = True
                        storage.all().pop(name_id_key)
                        storage.save()
                        storage.reload()
                        break
                if not found:
                    print("** no instance found **")
        else:
            print("** class name missing **")

        # if line:
        #    class_name = line.split(" ")[0]
        #    if class_name in HBNBCommand.class_names_list:
        #        length = len(line.split(" "))
        #        if length >= 2:
        #            match = False
        #            dictionary = storage.all()
        #            id = line.split(" ")[1]
        #            for key, value in dictionary.items():
        #                id_key = key.split(".")[1]
        #                if id == id_key:
        #                    match = True
        #                    key = key
        #                    break
        #            if match:
        #                dictionary.pop(key)
        #                storage.save()
        #                storage.reload()
        #            else:
        #                print("** no instance found **")
        #        else:
        #            print("** instance id missing **")
        #    else:
        #        print("** class doesn't exist **")
        # else:
        #    print("** class name missing **")

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

    def do_update(self, args):
        """update: update an instance based on the classname and id
        usage: update <class name> <id> <attribute name> "<attribute value>
        """
        arg = args.split()
        sw = 0
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.class_names_list:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif len(arg) < 3:
            print("** attribute name missing **")
        elif len(arg) < 4:
            print("** value missing **")
        else:
            in_key = (arg[0] + "." + arg[1])
            for key, obj in storage.all().items():
                if key == in_key:
                    idx_arg = len(arg[0]) + len(arg[1]) + len(arg[2]) + 3
                    value = args[idx_arg:]
                    if args[idx_arg] == "\"":
                        idx_arg += 1
                        value = args[idx_arg:-1]
                    if hasattr(obj, arg[2]):
                        value = type(getattr(obj, arg[2]))(args[idx_arg:])
                    setattr(obj, arg[2], value)
                    sw = 1
                    storage.save()
            if sw == 0:
                print("** no instance found **")

    # methods to exit the program
    def do_quit(self, line):
        """Quit: command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF: Ctrl-D working to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
