#!/usr/bin/python3
""" create a unique FileStorage instance for your application """

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from os import getenv



storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
