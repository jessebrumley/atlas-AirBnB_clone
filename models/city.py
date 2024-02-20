#!/usr/bin/python3
"""
Module defining City -> BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):

    state_id = ""  # will be State.id
    name = ""
