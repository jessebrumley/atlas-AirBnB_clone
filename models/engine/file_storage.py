#!/usr/bin/python3
"""
This module contains the FileStorage class
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __objects = {}
    __file_path = "file.json"

    def all(self, class_name=None):
        """
        Returns the dictionary __objects. Optionally filters by class_name.
        """
        if class_name is not None:
            pass
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in __objects with key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialized __objects to JSON file path
        """
        obj_dict = dict()
        for key, value in self.__objects.items():
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps(obj_dict))

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass


@property
def file_path(self):
    return self.__file_path
