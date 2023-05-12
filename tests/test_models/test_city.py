#!/usr/bin/python3
"""This is a Test suite for city class from models.city module"""

import unittest
from models.base_model import BaseModule
from models.city import City


class TestCity(unittest.TestCase):
    """This is Test case for City class"""

    def setUp(self):
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_city_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
        self.assertIs(type(getattr(self.city, attr)), str)
        self.assertFalse(bool(getattr(self.city,attr))) 
