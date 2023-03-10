#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """File Storage class
    With Methods and variables
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json_str = json.dumps(self.__objects)
            f.write(json_str)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                loaded_content = f.read()
                self.__objects = json.loads(loaded_content)
        except FileNotFoundError:
            pass
