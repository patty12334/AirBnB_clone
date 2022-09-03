#!/usr/bin/python3
from models.base_model import BaseModel
"""Define the Review Class that inherits from BaseModel."""


class Review(BaseModel):
    """Represents a Review.
    Attr:
        place_id (str): The id of the Place.
        user_id (str): The id of the User.
        text (str): The Review Text
    """

    place_id = ""
    user_id = ""
    text = ""
