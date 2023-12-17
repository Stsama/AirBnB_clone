#!/usr/bin/python3
# Albert Ezoula
# models/engine/file_storage.py
"""Represent a FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cob = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cob, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj] for obj in odict.key()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file)"""
        try:
            with open(FileStorage.__file_path? "r") as f:
                test = json.loads(f)
                for o in test.values():
                    cls_name = o["__class__"]
                    del o["__name__"]
                    self.new(eval(clas_name__)(**0))
        expect FileNotFoundError:
            return

