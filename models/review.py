#!/usr/bin/python3
"""
This is Review subclass  model that inherits from BaseModel parent class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A Review subclass that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
