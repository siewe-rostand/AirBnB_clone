#!/usr/bin/python3
"""
Unittest for user.py
"""
import unittest
from models.user import User
import datetime


class UserCase(unittest.TestCase):
    """
    Instances attribute and methods from user class
    """

    u = User()

    def test_class_exists(self):
        """
        class existence
        """
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_user_inheritance(self):
        """
        User is a subclass of BaseModel
        """
        self.assertIsInstance(self.u, User)

    def testHasAttributes(self):
        """
        Attributes existence verification test
        """
        self.assertTrue(hasattr(self.u, 'email'))
        self.assertTrue(hasattr(self.u, 'password'))
        self.assertTrue(hasattr(self.u, 'first_name'))
        self.assertTrue(hasattr(self.u, 'last_name'))
        self.assertTrue(hasattr(self.u, 'id'))
        self.assertTrue(hasattr(self.u, 'created_at'))
        self.assertTrue(hasattr(self.u, 'updated_at'))

    def test_types(self):
        """
        Attribute correctness verification Test
        """
        self.assertIsInstance(self.u.first_name, str)
        self.assertIsInstance(self.u.last_name, str)
        self.assertIsInstance(self.u.email, str)
        self.assertIsInstance(self.u.password, str)
        self.assertIsInstance(self.u.id, str)
        self.assertIsInstance(self.u.created_at, datetime.datetime)
        self.assertIsInstance(self.u.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
