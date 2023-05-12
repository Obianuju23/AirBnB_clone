#!/usr/bin/python3
"""This is a test suit for Amenity class from the models.state module"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """This is the Amenity class TestCase"""

    def setUp(self):
        self.amenity = Amenity()

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.amenity, BaseModel))

    def test_attr_is_a_class_attr(slf):
        self.assertTrue(hasattr(self.amenity == "name"))

    def test_class_attrs(self):
        self.assertsIs(type(self.amenity.name), str)
        self.assertFalse(bool(self.amenity.name))
