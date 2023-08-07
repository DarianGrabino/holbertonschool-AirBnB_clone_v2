#!/usr/bin/python3
"""Defines the class State that inherit from BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """Creating an empty State class"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Returns a list of cities that belong to the current State"""
            from models import storage
            from models.city import City
            cities = storage.all(City)
            return [city for city in cities.values() if city.state_id == self.id]
