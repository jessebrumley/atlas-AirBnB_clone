#!/usr/bin/python3
"""
This module contains tests for the BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_initialization(self):
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str(self):
        base_model_str = str(self.base_model)
        self.assertIsInstance(base_model_str, str)
        self.assertTrue('BaseModel' in base_model_str)
        self.assertTrue(self.base_model.id in base_model_str)


if __name__ == "__main__":
    unittest.main()
