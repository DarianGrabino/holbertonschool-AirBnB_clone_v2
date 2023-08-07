#!/usr/bin/python3
""" BaseModel class that defines all
    common attributes/methods for other classes """

import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """ BaseModel class that defines all """

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    time_value = datetime.strptime(value,
                                                   "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time_value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """ returns a string representation of the class
            instance attributes """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary of the class
            instance attributes  """
        new_dict = self.__dict__.copy()
        new_dict.pop("_sa_instance_state", None)
        new_dict["__class__"] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """ deletes the current instance from the storage """
        models.storage.delete(self)
