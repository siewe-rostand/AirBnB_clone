#!/usr/bin/python3

"""
Class that store and serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage:
    """
    class to manage stored json objects (model)
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        return the dictionary objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key class id
        """

        key = obj.__class__.name + '.' + + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        _dict = {}

        for k, v in FileStorage.__objects.items():
            _dict[k] = v.to_dict()

        with open(FileStorage.__file_path, 'W') as f:
            json.dump(_dict, f)

    def reload(self):
        """
        method to deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel

        dic = {'BaseModel': BaseModel}

        try:
            tmp = {}
            with open(FileStorage.__file_path, 'r') as f:
                tmp = json.load(f)
                for k, v in tmp.items():
                    self.all()[k] = dic[v['__class__']](**v)
        except FileNotFoundError:
            pass
