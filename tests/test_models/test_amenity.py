#!/usr/bin/python3
"""This is a test suit for Amenity class from the models.state module"""

import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """This is the Amenity class TestCase"""

    def setUp(self):
        """used to setup the test"""
        pass

    def tearDown(self):
        """used to destroy the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_amenity_is_a_subclass_of_basemodel(self):
        """tests that is a subclass of BaseModel"""
        my_amenity = Amenity()
        self.assertTrue(issubclass(type(my_amenity), BaseModel))

    def test_doc(self):
        """check that the class is documented"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_attr(self):
        """checks that amenity has the right attributes"""
        amenity = Amenity()
        amenity.name = "Air Condition"
        self.assertTrue('id' in amenity.__dict__)
        self.assertTrue('created_at' in amenity.__dict__)
        self.assertTrue('updated_at' in amenity.__dict__)
        self.assertTrue('name' in amenity.__dict__)

    def test_name(self):
        """checks that the date time is string"""
        amenity = Amenity()
        amenity.name = "Air Condition"
        self.assertEqual(type(amenity.name), str)

    def test_save(self):
        """check that the save function work"""
        amenity = Amenity()
        amenity.save()
        second_amenity = Amenity()
        second_amenity.save()
        self.assertFalse(amenity.updated_at is amenity.created_at)
        self.assertNotEqual(amenity.created_at, second_amenity.created_at)
        self.assertNotEqual(amenity.id, second_amenity.id)

    def test_to_dict(self):
        """checks that the to_dict function works"""
        amenity = Amenity()
        amenity.name = "Fan"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], 'Fan')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
