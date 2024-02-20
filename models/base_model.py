#!/usr/bin/python3
"""
This module defines the BaseModel class, parent for all other classes
"""
from datetime import datetime
import uuid
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        """
        Initialization for BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key != '__class__':
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        if not kwargs:
            models.storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates updated_at with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        if isinstance(self.created_at, datetime):
            obj_dict['created_at'] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
