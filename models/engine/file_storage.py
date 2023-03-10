#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """File Storage class
    With Methods and variables
    """

    def __init__(self):
        """Constructor"""
        self.__file_path = "../../file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key"""
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()
        print(self.__objects)

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json_str = json.dumps(self.__objects)
            print(json_str)
            f.write(json_str)

    def reload(self):
        """deserializes the JSON file to __objects"""
