#!/usr/bin/python3
"""
This model defines FileStorage class
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """ The FileStorage Class """

    __file_path = "file.json"
    __objects = dict()
    classes = {"BaseModel": BaseModel}

    def all(self):
        """Returns a dictionary of all objects by <class name>.id"""
        return self.__objects

    def new(self, obj):
        """sets in _objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        mydict = dict()
        for key, value in self.__objects.items():
            mydict[key] = value.to_dict()
        with open(self.__file_path, "w") as myFile:
            json.dump(mydict, myFile)

    def reload(self):
        """deserializes the json file to __objects if it meets requirements"""
        try:
            with open(self.__file_path, "r") as myFile:
                objects = json.load(myFile)
            for key, value in objects.items():
                if value["__class__"] == "BaseModel":
                    obj = BaseModel(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
