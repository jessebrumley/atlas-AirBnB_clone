#!/usr/bin/python3
"""
Module containing unittests for REview class
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        self.review_model = Review()

    def test_initialization(self):
        self.assertIsInstance(self.review_model.place_id, str)
        self.assertIsInstance(self.review_model.text, str)


if __name__ == "__main__":
    unittest.main()
