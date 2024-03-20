#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


place_amenity = Table("place_amenity", metadata=Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), nullable=False, ForeignKey=(cities.id))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, defeult=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref=backref('place'))
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """getter of the relatioship between Place and Review"""
            all_reviews = models.storage.all(Review)
            place_reviews = []
            for key, val in all_reviews.items():
                if val.place.id == self.id:
                    place_reviews.append(val)
            return place_review

        @property
        def amenities(self):
            """getter of the relationship between Place and Amenity"""
            all_amenities = models.storage.all(Amenity)
            place_amenities = []
            for key, val in all_amenities.items():
                if val.id in self.amenity_ids:
                    place_amenities.append(val)
            return place_amenities

        @amenities.setter
        def amenities(self, obj):
            """Setter for amenities"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
            else:
                return
