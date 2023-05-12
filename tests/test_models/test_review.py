#!/usr/bin/python3
"""This is Test suite for Review class from models.review"""

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """Test case for Review class"""

    def setUp(self):
        self.review = Review()
        self.attr_list = ["place_id", "user_id", "text"]

    def test_review_is_a_subclass_of_basemodel(self):
        self.assertTrue(type(self.review, BaseModel)

    def test_attr_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(Review, attr))

    def test_class_attrs(self):
        self.assertIs(type(self.review.place_id)), str)
        self.assertIs(type(self.review.user_id)), str)
        self.assertIs(type(self.review.text)), str)

    for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.review, attr)))
