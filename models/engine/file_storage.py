#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            _dct = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(_dct, f)


    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as f:
                for k, v in json.load(f).items():
                    self.new(dct[v['__class__']](**v))
