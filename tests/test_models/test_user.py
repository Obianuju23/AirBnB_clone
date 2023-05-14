#!/usr/bin/python3
"""This is a test suite for User class in models.user"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def setUp(self):
        """used to set up the test"""
        pass

    def tearDown(self):
        """used to destroy the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attrs_are_class_attrs(self):
        """tests that the attributes are present"""
        u = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "email")
                        and hasattr(User, "password"))

    def test_class_attrs(self):
        """tests that attributes is of the right type"""
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertIs(type(u.email), str)
        self.assertIs(type(u.password), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")
        self.assertTrue(u.email == "")
        self.assertTrue(u.password == "")

    def test_user_is_a_subclass_of_basemodel(self):
        """tests that attribute is a subclass of basemodel"""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_save(self):
        """tests that the save function works"""
        u = User()
        u.save()
        u1 = User()
        u1.save()
        self.assertFalse(u.updated_at is u.created_at)
        self.assertNotEqual(u.updated_at, u1.updated_at)
        self.assertNotEqual(u.id, u1.id)

    def test_to_dict(self):
        """tests that the to_dict function works"""
        u = User()
        u_dict = u.to_dict()
        self.assertIsInstance(u_dict['created_at'], str)
        self.assertIsInstance(u_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
