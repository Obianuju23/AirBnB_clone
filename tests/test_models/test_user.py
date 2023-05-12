#!/usr/bin/python3
"""This is a test suite for User class in models.user"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attrs_are_class_attrs(self):
        u = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "email")
                        and hasattr(User, "password"))

    def test_class_attrs(self):
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
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel)
