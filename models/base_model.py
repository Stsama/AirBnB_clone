#!/usr/bin/python3
# models/base_model.py
# Created by Albert Ezoula
"""Define a base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents a base model"""

    def __init__(self, *args, **kwargs):
        """
            Initialize the Basemodel instance
                Args:
                    *args(list): unused
                    **kwargs(dict): Dictiopnnary of arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs and kwargs != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.today()
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["created_at"] = str(datetime.today().isoformat())
        rdict["updated_at"] = str(datetime.today().isoformat())
        return rdict
