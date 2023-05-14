#!/usr/bin/python3
"""A subclass city inheriting from parentclass BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """This City class inherited from BaseModel class"""

    state_id = ""
    name = ""
