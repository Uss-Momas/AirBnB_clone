#!/usr/bin/python3
"""file_storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All method"""
        return FileStorage.__objects

    def new(self, obj):
        """new object method"""
        if obj:
            key = type(obj).__name__ + "." + obj.id
            # print(key)
            FileStorage.__objects[key] = obj

    def save(self):
        """Save file
        Serializes the python object to be a json string
        """
        objects_dictionary = {}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            for key, obj in FileStorage.__objects.items():
                # print("Key: ", key)
                # print("Value: ", obj)
                # print("Object dictionary: ", obj_dict)
                objects_dictionary[key] = obj.to_dict()
                # print(objects_dictionary)
            json_str = json.dumps(objects_dictionary)
            # print(json_str)
            f.write(json_str)

    def reload(self):
        """Reload method
        Reload the json information from a file and deserialize it to be
        python obj
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                content = f.read()
                json_loaded = json.loads(content)
                # print(json_loaded)
                for key, value in json_loaded.items():
                    # print("Key: ", key)
                    # print("Value: ", value)
                    if key.split(".")[0] == "BaseModel":
                        obj = BaseModel(**value)
                    elif key.split(".")[0] == "User":
                        obj = User(**value)
                    elif key.split(".")[0] == "Place":
                        obj = Place(**value)
                    elif key.split(".")[0] == "City":
                        obj = City(**value)
                    elif key.split(".")[0] == "State":
                        obj = State(**value)
                    elif key.split(".")[0] == "Amenity":
                        obj = Amenity(**value)
                    elif key.split(".")[0] == "Review":
                        obj = Review(**value)
                    FileStorage.__objects[key] = obj
                    # print(obj)
        except Exception:
            pass
