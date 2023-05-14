#!/usr/bin/python3
"""
This Place subclass  model inherited from parent class BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This is a subclass Place that inherits from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]
