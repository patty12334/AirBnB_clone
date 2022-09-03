#!/usr/bin/python3
from models.base_model import BaseModel
"""Define the City Class that inherits from BaseModel."""


class City(BaseModel):
    """Represents a city.
    Attr:
        name (str): The name of the City.
        state_id (str): The id of the State.
    """

    name = ""
    state_id = ""
