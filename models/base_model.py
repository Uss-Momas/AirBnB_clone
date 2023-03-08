#!/usr/bin/python3
"""Base Model module
defines all common attributes/methods for other classes
"""
from datetime import datetime
from datetime import date
import time


class BaseModel:
    """BaseModel class that contains every method that we are going to use"""
    updated_at = datetime.now()

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
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
