#!/usr/bin/python3
"""
This model defines FileStorage class
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ The FileStorage Class """

    __file_path = "file.json"
    __objects = dict()
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

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
                class_name = value.get("__class__")
                if class_name in self.classes:
                    class_obj = self.classes[class_name]
                    obj = class_obj(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
