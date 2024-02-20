#!/usr/bin/python3
"""
Module containing unittests for User class
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_model = User()

    def test_initialization(self):
        self.assertIsInstance(self.user_model.email, str)
        self.assertIsInstance(self.user_model.password, str)
        self.assertIsInstance(self.user_model.first_name, str)
        self.assertIsInstance(self.user_model.last_name, str)


if __name__ == "__main__":
    unittest.main()
