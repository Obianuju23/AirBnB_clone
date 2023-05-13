#!/usr/bin/python3
"""This is a Test suite for city class from models.city module"""

import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """This is Test case for City class"""

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_city_is_a_subclass_of_basemodel(self):
        city = City()
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_doc(self):
        """check that the class is documented"""
        self.assertIsNotNone(City.__doc__)

    def test_attr(self):
        """checks that amenity has the right attributes"""
        city = City()
        city.state_id = "54"
        city.name = "Benin"
        self.assertTrue('id' in city.__dict__)
        self.assertTrue('created_at' in city.__dict__)
        self.assertTrue('updated_at' in city.__dict__)
        self.assertTrue('name' in city.__dict__)
        self.assertTrue('state_id' in city.__dict__)

    def test_name_and_state(self):
        city = City()
        city.state_id = "54"
        city.name = "Benin"
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)
    
    def test_save(self):
        """test that the save function works"""
        city = City()
        city.save()
        second_city = City()
        second_city.save()
        self.assertFalse(city.id == second_city.id)
        self.assertNotEqual(city.created_at, city.updated_at)
        self.assertNotEqual(city.created_at, second_city.updated_at)

    def test_to_dict(self):
        """tests that the to_dict function works"""
        city = City()
        city.state_id = "54"
        city.name = "Benin"
        city_dict = city.to_dict()
        self.assertEqual(city_dict['state_id'], "54")
        self.assertEqual(city_dict['name'], "Benin")
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
