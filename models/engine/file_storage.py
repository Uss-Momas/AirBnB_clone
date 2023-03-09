#!/usr/bin/python3
"""File Storage Module"""


class FileStorage:
    """File Storage class
    With Methods and variables
    """

    def __init__(self):
        """Constructor"""
        self.__file_path = ""
        self.__objects = {}
        ...

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self):
        """Sets in __objects the obj with key"""

    def save(self):
        """Serializes __objects to the JSON file"""

    def reload(self):
        """deserializes the JSON file to __objects"""
