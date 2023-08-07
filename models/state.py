#!/usr/bin/python3
"""Defines the class State that inherit from BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """Creating an empty State class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable = False)
    cities = relationship("City", backref = "state", cascade = "all, delete")

    def cities(self):
        """Returns a list of City instances with state_id equals to the
        current State.id"""
        from models import storage
        from models.city import City
        cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
                return cities
