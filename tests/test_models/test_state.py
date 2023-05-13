#!/usr/bin/python3
"""This is a test suit for State class from the models.state module"""

import unittest
import os
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """This is the State class TestCase"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_state_is_a_subclass_of_basemodel(self):
        """test if class is a subclass of BaseModel"""
        state = State()
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_doc(self):
        """test that the class is documented"""
        self.assertIsNotNone(State.__doc__)

    def test_attr(self):
        """tests the attributes type"""
        state = State()
        state.name = "Edo"
        self.assertTrue('id' in state.__dict__)
        self.assertTrue('created_at' in state.__dict__)
        self.assertTrue('updated_at' in state.__dict__)
        self.assertTrue('name' in state.__dict__)

    def test_name_type(self):
        """tests that the attribute is of correct type"""
        state = State()
        state.name = "Edo"
        self.assertEqual(type(state.name), str)
        self.assertIs(type(state.name), str)

    def test_save(self):
        """test that the save function works"""
        state = State()
        state.save()
        second_state = State()
        second_state.save()
        self.assertFalse(state.updated_at is state.created_at)
        self.assertNotEqual(state.created_at, second_state.created_at)
        self.assertNotEqual(state.id, second_state.id)

    def test_to_dict(self):
        """test that the to_dict function works"""
        state = State()
        state.name = "Edo"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "Edo")
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
