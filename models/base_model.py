#!/usr/bin/python3

"""
this is the base class to be inherited by other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    All the class attributes and methods are defined here
    """

    def __init__(self, *args, **kwargs):
        """
        attributes initialization
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            _f = '%Y-%m-%d%T%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, _f)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        return the class name,id and dictionary attributes
        """
        class_name = "[" + self.__class__.__name__ + "]"
        _dic = {k: v for (k, v) in self.__dict__.items() if (not v) is false}
        return class_name + "(" + self.id + ")" + str(_dic)

    def save(self):
        """
        update the updated_at attribute to current time
        """
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        return a new dictionary and dtatimes as string
        """

        new_dictionary = {}

        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                new_dictionary[k] = v.isoformat()
            else:
                new_dictionary[k] = v
        new_dictionary["__class__"] = self.__class__.__name__

        return new_dictionary
