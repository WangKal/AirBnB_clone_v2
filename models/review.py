#!/usr/bin/python3
"""Defines a class Review"""
from models.base_model import BaseModel


class Review (BaseModel):
    """Class that defines Review .

    Attributes:
        place_id (string): id of city.
        user_id (string): id of user.
        text (string): just a text.
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """New instances of Review.
        """
        super().__init__(*args, **kwargs)
