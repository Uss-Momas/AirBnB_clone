#!/usr/bin/python3
"""
Base class for the project
"""

from uuid import uuid4
from datetime import datetime
import models
class BaseModel:
    """It is  a base for all the classes in the AirBnb project
    Arttributes:
        id(str): user identity
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at:  datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
    Methods:
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>, it prints the class name,id and dict
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
    """
    def __init__(self,*args,**kwargs):
        """
        Initialize attributes

        args:
            args:handles keyword arguments
            kwargs:it will work as a dict
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

        def __str__(self):
            """
            it prints the class name,id and dict
            """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

