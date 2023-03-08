#!/usr/bin/python3
"""Base Model module
defines all common attributes/methods for other classes
"""
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class that contains every method that we are going to use"""
    def __init__(self):
        """Constructor of the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""
        cls_name = type(self).__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """method to update public instance attribute updated_at
        with the current datetime
        """
        # time.sleep(5)
        self.updated_at = datetime.now()

    def to_dict(self):
        """Method that:
        Returns a dictionary containing all keys/values of __dict__
        """
        dictionary = self.__dict__
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
