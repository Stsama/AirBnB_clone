#!/usr/bin/python3
# models/base_model.py
# Created by Albert Ezoula
"""Define a base class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents a base model"""

    def __init__(self, id=uuid4(), created_at=datetime.today(),
                 updated_at=datetime.today()):
        """
            Initialize the Basemodel instance
                Args:
                id(string): assign with an uuid when an instance is created
                created_at(datetime): datetime when an instance is created
                updated_at(datetime): datetime when an instance is created and
                it will be updated every time you change your object
        """
        self.updated_at = updated_at
        self.id = str(id)
        self.created_at = created_at

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
