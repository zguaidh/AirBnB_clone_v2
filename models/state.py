#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', cascade='all, delete, delete-orphan',
            backref='state')

    @property
    def cities(self):
        """Fetches all cities that belong to this state
        """
        return [city for city in models.storage.all(City).values()
                if city.state_id == self.id]
