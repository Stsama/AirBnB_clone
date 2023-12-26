#!/usr/bin/python3
# created by ALBERT EZOULA
# models/engine/file_storage.py
"""Representes the Filestorage class"""
import os
from models.base_model import BaseModel
import json



class FileStorage:
    """Define erialization and deserialisation of object"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(self.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        all_objects = FileStorage.__objects
        one_object = {obj: all_objects[obj].to_dict() for obj in all_objects.keys()}
        with open(FileStorage.__file_path, "w+") as f:
            json.dump(one_object, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path) as f:
                all_objects = json.load(f)
                for o in all_objects.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        else:
            return
