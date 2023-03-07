#!/usr/bin/python3
"""Base Model module
defines all common attributes/methods for other classes
"""
import datetime


class BaseModel:
    """BaseModel class that contains every method that we are going to use"""

    def save(self):
        """method to update public instance attribute updated_at
        """
        ...

    def to_dict(self):
        """Method that:
        Returns a dictionary containing all keys/values of __dict__
        """
        ...
