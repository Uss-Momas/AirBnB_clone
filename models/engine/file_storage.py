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
        key = type(obj) + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(self.__file_path, encoding="utf-8") as f:
            json.dumps()

    def reload(self):
        """deserializes the JSON file to __objects"""
