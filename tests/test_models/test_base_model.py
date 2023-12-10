#!/usr/bin/python3
"""
base model class for Unittests
"""


import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import datetime


class test_basemodel(unittest.TestCase):
    """ class to test the base model attributes and method """

    @classmethod
    def setUpClass(clss):
        """
        Open test environment
        """
        cls.base_model = BaseModel()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(clss):
        """
        Close test environment
        """
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        """
        Checks if save method updates the public instance instance
        attribute updated_at
        """

        prev_date = self.base_model.updated_at
        self.base_model.save()
        self.assertGreater(self.base_model.updated_at, prev_date)
        self.assertTrue(os.path.exists("file.json"))

    def str_method_test(self):
        """
        tostring test
        """

        clss_name = str(self.base_model.__class__.__name__)
        obj_dict = str(self.base_model.__dict__)
        obj_str = f"[{cls_name}] ({self.base_model.id}) {obj_dict}"
        self.assertEqual(obj_str, self.base_model.__str__())

    def to_dict_test(self):
        """
        to_dict method test
        """

        dct = {
            "id": self.base_model.id,
            "__class__": self.base_model.__class__.__name__,
            "created_at": self.base_model.created_at.isoformat(),
            "updated_at": self.base_model.updated_at.isoformat()
        }
        self.assertDictEqual(dct, self.base_model.to_dict())

if __name__ == '__main__':
    unittest.main()
