#!/usr/bin/python3
""" FileStorage class """


from os.path import exists
import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in objects the obj with key <obj class name>.id """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        self.save()

    def save(self):
        """ serializes objects to the JSON file """
        dicts = {}
        for key, value in self.__objects.items():
            dicts[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dicts, f)

    def reload(self):
        """ deserializes the JSON file to objects """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dicts = json.load(f)
                for key, value in dicts.items():
                    self.__objects[key] = BaseModel(**value)
        else:
            pass

    def delete(self, obj=None):
        """Delete object"""
        if obj != None and obj.__class__.__name__ + "." + obj.id in self.__objects:
            del self.__objects[obj.__class__.__name__ + "." + obj.id]
