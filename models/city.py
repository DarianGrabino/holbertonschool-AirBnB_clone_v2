#!/usr/bin/python3
"""Defines the class City that inherit from BaseModel"""

from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """Create a new empty City class"""

    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"
