#!/usr/bin/python3
"""
Module containing unittests for State class
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.state_model = State()

    def test_initialization(self):
        self.assertIsInstance(self.state_model.name, str)


if __name__ == "__main__":
    unittest.main()
