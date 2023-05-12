#!/usr/bin/python3
"""This is a test suit for State class from the models.state module"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """This is the State class TestCase"""

    def setUp(self):
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state, BaseModel))

    def test_attr_is_a_class_attr(slf):
        self.assertTrue(hasattr(self.state == "name"))

    def test_class_attrs(self):
        self.assertsIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))
