#!/usr/bin/python3
"""
Module containing unittests for City class
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city_model = City()

    def test_initialization(self):
        self.assertIsInstance(self.city_model.state_id, str)
        self.assertIsInstance(self.city_model.name, str)


if __name__ == "__main__":
    unittest.main()
