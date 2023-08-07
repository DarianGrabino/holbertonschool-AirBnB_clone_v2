#!/usr/bin/python3
"""Defines the class User that inherit from BaseModel"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """Creates a new empty user"""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
