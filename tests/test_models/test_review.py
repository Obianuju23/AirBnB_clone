#!/usr/bin/python3
"""This is Test suite for Review class from models.review"""

import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for Review class"""

    def setUp(self):
        """used to setup the test"""
        pass

    def tearDown(self):
        """used to destroy the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_review_is_a_subclass_of_basemodel(self):
        """tests to check that the class review is a subclass"""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_doc(self):
        """tests that the class is documented"""
        self.assertIsNotNone(Review.__doc__)

    def test_attr_are_class_attrs(self):
        """tests that attributes are in class"""
        review = Review()
        review.place_id = "3"
        review.user_id = "54"
        review.text = "very good"
        self.assertTrue('id' in review.__dict__)
        self.assertTrue('created_at' in review.__dict__)
        self.assertTrue('updated_at' in review.__dict__)
        self.assertTrue('place_id' in review.__dict__)
        self.assertTrue('user_id' in review.__dict__)

    def test_class_types(self):
        """checks the type of attribute"""
        review = Review()
        self.assertIs(type(review.place_id), str)
        self.assertIs(type(review.user_id), str)
        self.assertIs(type(review.text), str)

    def test_save(self):
        """tests that the save function work"""
        review = Review()
        review.save()
        second_review = Review()
        review.save()
        self.assertFalse(review.updated_at is review.created_at)
        self.assertNotEqual(review.created_at, second_review.created_at)
        self.assertNotEqual(review.id, second_review.id)

    def test_to_dict(self):
        """test that the to_dict function works"""
        review = Review()
        review.place_id = "3"
        review.user_id = "54"
        review_dict = review.to_dict()
        self.assertEqual(review_dict['place_id'], '3')
        self.assertEqual(review_dict['user_id'], '54')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
