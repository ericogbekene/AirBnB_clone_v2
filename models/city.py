#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    _tablename__ = 'cities'
    state_id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
