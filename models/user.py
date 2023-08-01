#!/usr/bin/python3
"""Defines the class User that inherit from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new empty user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
