#!/usr/bin/python3
"""Defines the class Review that inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Create a new review empty class"""

    place_id = ""
    user_id = ""
    text = ""
