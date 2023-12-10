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
        return FileStorage.__objects

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

        dct = {
                    'BaseModel': BaseModel
                  }
        
        try:
            with open(self.__file_path, 'r') as f:
                dct = json.loads(f.read())
                for value in dct.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass
