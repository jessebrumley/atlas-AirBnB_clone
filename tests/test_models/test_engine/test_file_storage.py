#!/usr/bin/python3
"""
This module contains tests for the FileStorage class
"""
import unittest
import os
import json
from datetime import datetime
import uuid
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up environment for each test"""
        self.storage = FileStorage()
        self.file_path = self.storage.file_path

    def tearDown(self):
        """Clean environment after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_new_and_save(self):
        """Test adding new object and saving"""
        user = User(email="test@example.com")
        self.storage.new(user)
        self.storage.save()

    def test_base_model_save(self):
        """Test BaseModel save method"""
        model_instance = BaseModel()
        model_instance.id = str(uuid.uuid4())
        model_instance.created_at = datetime.now()
        model_instance.updated_at = model_instance.created_at
        model_instance.save()
        self.storage.reload()
        stored_instance = self.storage.all().get(f"{model_instance.__class__.__name__}.{model_instance.id}")
        self.assertIsNotNone(stored_instance, "The instance should be present in storage after the save.")
        self.assertIsInstance(stored_instance, type(model_instance))

    def test_reload(self):
        """Test reloading from save"""
        user = User(id="1", email="test@example.com")
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        loaded_user = self.storage.all().get("User.1")
        self.assertIsInstance(loaded_user, User)
        self.assertEqual(loaded_user.email, "test@example.com")

if __name__ == '__main__':
    unittest.main()
