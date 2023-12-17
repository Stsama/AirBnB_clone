#!/usr/bin/python3
# models/base.py
# Albert Ezoula
"""Define a class Base"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent the basemodel class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.today().isoformat()
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        sdict = self.__dict__.copy()
        sdict["created_at"] = str(datetime.today().isoformat())
        sdict["updated_at"] = str(datetime.today().isoformat())
        sdict["__class__"] = self.__class__.__name__
        return sdict

    def __str__(self):
        """Prints the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
