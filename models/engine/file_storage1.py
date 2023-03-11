#!/usr/bin/python3
"""File Storage Module"""
import json
from models.base_model import base_model


class FileStorage:
    """File Storage class
    With Methods and variables
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        print(obj)
        if obj:
            key = type(obj).__name__ + "." + obj.id
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        dictionary = {}
        for k, obj in FileStorage.__objects.items():
            dictionary[k] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json_str = json.dumps(dictionary)
            f.write(json_str)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                loaded_content = f.read()
                loaded_dictionary = json.loads(loaded_content)
                for key, obj_dict in loaded_dictionary.items():
                    new_obj = eval(obj_dict['__class__'])(**obj_dict)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            pass
