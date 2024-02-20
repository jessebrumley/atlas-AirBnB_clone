#!/usr/bin/python3
"""
Module containing unittests for Amenity class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity_model = Amenity()

    def test_initialization(self):
        self.assertIsInstance(self.amenity_model.name, str)


if __name__ == "__main__":
    unittest.main()
