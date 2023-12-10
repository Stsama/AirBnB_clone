#!/usr/bin/python3
# models/base.py
# Albert Ezoula
"""Define a class Base"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represent the basemodel class"""

    def __init__(self, id=uuid4(), created_at=datetime.today(),
                 updated_at=datetime.today()):
        """Initialisation of an instance of baseClass
            Args:
                id(str): assign with an uuid when an instance is created
                created_at(datetime): current datetime when
                                      an instance is created
                updated_at(datetime): current datetime when
                                      an instance is created
        """
        self.id = str(id)
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """Prints the string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        sdict = self.__dict__.copy()
        sdict["__class__"] = self.__class__.__name__
        sdict["created_at"] = str(datetime.today().isoformat())
        sdict["updated_at"] = str(datetime.today().isoformat())
        return sdict
