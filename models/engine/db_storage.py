#!/usr/bin/python3
"""DBStorage Egine
"""
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Class for db storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a DB storage"""
        HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                    HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                pool_pre_ping=True)

        if os.environ.get("HBNB_ENV", "dev") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects on a table"""
        if cls is None:
            objs = self.__session.query(User).all()
            objs.extend(self.__session.query(State).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Amenity).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add object (obk) to current session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine,
                expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
