#!/usr/bin/python3
""" State Module for HBNB project """
import os

import models
from models.base_model import BaseModel, Base
from models.city import City

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            back_populates='state',
            cascade="all, delete, delete-orphan")

    if os.environ.get("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    def __repr__(self):
        """Representation of a State object"""
        string = "<State(name='{}')>".format(self.name)
        return string
