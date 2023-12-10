#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ 
    Instances attributes and methods from State class
    """

    s = State()

    def test_class_exists(self):
        """
        class existence test
        """
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.s)), res)

    def test_user_inheritance(self):
        """
        State is a subclass of BaseModel
        """
        self.assertIsInstance(self.s, State)

    def testHasAttributes(self):
        """
        attributes existence verification test
        """
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))

    def test_types(self):
        """
        attribute correctness Test
        """
        self.assertIsInstance(self.s.name, str)
        self.assertIsInstance(self.s.id, str)
        self.assertIsInstance(self.s.created_at, datetime.datetime)
        self.assertIsInstance(self.s.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
