#!/usr/bin/python3

"""
base model class for Unittests
"""


import unittest
from models.base_model import BaseModel
import os
from models import storage
from models.engine.file_storage import FileStorage
import datetime


class TestBaseModel(unittest.TestCase):
    """
    base model attributes and method test cases
    """

    _model = BaseModel()

    def baseModelTest1(self):
        """
        Test base model attributes
        """

        self._model.name = 'BaseModel'
        self._model.save()
        json_model = self._model.to_dict()

        self.assertEqual(sel._model.name, json_model['name'])
        self.assertEqual(self._model.name, json_model['__class__'])
        self.assertEqual(self._model.id, json_model['id'])

    def saveTest(self):
        """
        method to test save method
        """

        self._model.course = 'alx_se'
        self._model.save()

        self.assertIsInstance(self._model.id, str)
        self.assertIsInstance(self._model.created_at, datetime.datetime)
        self.assertIsInstance(self._model.updated_at, datetime.datetime)

        f_dic = self._model.to_dict()

        self._model.course = 'alx_cloud'

        sec_dict = self._model.to_dict()

        self.assertEqual(f_dic['created_at'], sec_dict['created_at'])
        self.assertNotEqual(f_dic['updated_at'], sec_dict['updated_at'])


if __name__ == "__main__"
unittest.main()
