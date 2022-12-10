#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.place import *
from models.state import *
from models.amenity import *
from models.user import *
from models.review import *
from models.city import *

HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
