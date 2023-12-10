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
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
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
        return a new dictionary and datetimes as string
        """

        new_dictionary = self.__dict__.copy()

        new_dictionary["__class__"] = self.__class__.__name__
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()

        return new_dictionary
