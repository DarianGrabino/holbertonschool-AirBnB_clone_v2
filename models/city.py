#!/usr/bin/python3
"""Defines the class City that inherit from BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """Create a new empty City class"""

    __tablename__ = 'cities'
    name = Column(String(128), nullable = False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable = False)
