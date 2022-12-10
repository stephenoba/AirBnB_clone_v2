#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review


place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id', String(60),
            ForeignKey('places.id'), primary_key=True),
        Column(
            'amenity_id', String(60),
            ForeignKey('amenities.id'), primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(
            String(60),
            ForeignKey('cities.id'),
            nullable=False)
    city = relationship("City", back_populates="places")
    user_id = Column(
            String(60),
            ForeignKey('users.id'),
            nullable=False)
    user = relationship("User", back_populates="places")
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship(
            "Review",
            back_populates='place',
            cascade="all, delete, delete-orphan")
    amenities = relationship(
            'Amenity',
            secondary='place_amenity',
            viewonly=False)
    amenity_ids = []

    if os.environ.get("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Get a list of all related City objects."""
            reviews_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews_list.append(city)
            return reviews_list

        @property
        def amenities(self):
            """Get list of all related amenities"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            """Set a new amenity"""
            from models.amenity import Amenity

            if type(value) != Amenity:
                if value.place_id == self.id:
                    self.amenity_ids.append(value)
