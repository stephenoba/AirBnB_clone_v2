#!/usr/bin/python3
"""This module defines a class User"""
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship(
                "Place",
                back_populates='user',
                cascade="all, delete, delete-orphan")
        reviews = relationship(
                "Review",
                back_populates='user',
                cascade="all, delete, delete-orphan")
