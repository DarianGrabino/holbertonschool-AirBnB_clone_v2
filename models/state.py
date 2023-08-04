#!/usr/bin/python3
"""Defines the class State that inherit from BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """Creating an empty State class"""

    
    __tablename__ = 'states'
    name = Column(String(128), nullable = False)
    cities = relationship("City", backref = "state", cascade = "all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        def cities(self):
            """Return the list of cities associated with the current state"""
            from models import storage
            from models.city import City
            asociated_cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    asociated_cities.append(city)
            return asociated_cities
