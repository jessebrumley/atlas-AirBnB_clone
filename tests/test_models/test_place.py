#!/usr/bin/python3
"""
Module containing unittests for Place class
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place_model = Place()

    def test_initialization(self):
        self.assertIsInstance(self.place_model.city_id, str)
        self.assertIsInstance(self.place_model.user_id, str)
        self.assertIsInstance(self.place_model.name, str)
        self.assertIsInstance(self.place_model.description, str)
        self.assertIsInstance(self.place_model.number_bathrooms, int)
        self.assertIsInstance(self.place_model.number_bathrooms, int)
        self.assertIsInstance(self.place_model.max_guest, int)
        self.assertIsInstance(self.place_model.price_by_night, int)
        self.assertIsInstance(self.place_model.latitude, float)
        self.assertIsInstance(self.place_model.longitude, float)
        self.assertIsInstance(self.place_model.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
