#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

from models.place import *
from models.state import *
from models.amenity import *
from models.user import *
from models.review import *
from models.city import *

HBNB_TYPE_STORAGE = os.environ.get("HBNB_TYPE_STORAGE", "db")

if HBNB_TYPE_STORAGE == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
