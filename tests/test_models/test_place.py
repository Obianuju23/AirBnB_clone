#!/usr/bin/python3
"""This is a Test suite for Place class from models.place module"""

import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """This is Test case for City class"""
 
    def setUp(self):
        """used to set up the test"""
        pass

    def tearDown(self):
        """used to destory the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_place_is_a_subclass_of_basemodel(self):
        """test is place if a subclass of BaseModel"""
        place = Place()
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attrs(self):
        """checks that amenity has the right attributes"""
        place = Place()
        place.city_id = "34"
        place.user_id = "OmobaVII"
        place.name = "Nigeria"
        place.description = "A place in africa"
        place.number_rooms = 5
        place.number_bathrooms = 2
        place.max_guest = 4
        place.price_by_night = 4000
        place.latitude = 6.34
        place.longitude = 5.46
        place.amenity_ids = ["AC"]
        self.assertTrue("id" in place.__dict__)
        self.assertTrue("created_at" in place.__dict__)
        self.assertTrue("updated_at" in place.__dict__)
        self.assertTrue("city_id" in place.__dict__)
        self.assertTrue("user_id" in place.__dict__)
        self.assertTrue("name" in place.__dict__)
        self.assertTrue("description" in place.__dict__)
        self.assertTrue("number_rooms" in place.__dict__)
        self.assertTrue("number_bathrooms" in place.__dict__)
        self.assertTrue("max_guest" in place.__dict__)
        self.assertTrue("price_by_night" in place.__dict__)
        self.assertTrue("latitude" in place.__dict__)
        self.assertTrue("longitude" in place.__dict__)
        self.assertTrue("amenity_ids" in place.__dict__)
        

    def test_attrs_type(self):
        """tests the type of the attributes"""
        place = Place()
        self.assertEqual(type(place.city_id), str)
        self.assertEqual(type(place.user_id), str)
        self.assertEqual(type(place.name), str)
        self.assertEqual(type(place.description), str)
        self.assertEqual(type(place.number_rooms), int)
        self.assertEqual(type(place.number_bathrooms), int)
        self.assertEqual(type(place.max_guest), int)
        self.assertEqual(type(place.price_by_night), int)
        self.assertEqual(type(place.latitude), float)
        self.assertEqual(type(place.longitude), float)
        self.assertEqual(type(place.amenity_ids), list)

    def test_save(self):
        """tests that the save function works"""
        place = Place()
        place.save()
        second_place = Place()
        place.save()
        self.assertFalse(place.updated_at is place.created_at)
        self.assertNotEqual(place.created_at, second_place.created_at)
        self.assertNotEqual(place.id, second_place.id)

    def test_to_dict(self):
        """test that the to_dict function works"""
        place = Place()
        place.name = "Nigeria"
        place.latitude = 6.34
        place.amenity_ids = ["34"]
        place.price_by_night = 4000
        place_dict = place.to_dict()
        self.assertEqual(place_dict['name'], 'Nigeria')
        self.assertIsInstance(place_dict['name'], str)
        self.assertIsInstance(place_dict['latitude'], float)
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['amenity_ids'], list)
        self.assertIsInstance(place_dict['price_by_night'], int)

if __name__ == "__main__":
    unittest.main()
