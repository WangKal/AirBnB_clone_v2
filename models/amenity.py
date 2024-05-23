#!/usr/bin/python3
"""Defines a class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that defines Amenity.

    Attributes:
        name (string): name of the amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """New instances of Amenity.
        """
        super().__init__(*args, **kwargs)
