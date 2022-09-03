#!/usr/bin/python3
from models.base_model import BaseModel
"""Define the User Class that inherits from BaseModel."""


class User(BaseModel):
    """Represents a User.
    Attr:
        email (str): The email address of the User.
        password (str): The password of the User.
        first_name (str): The first name of the User.
        last_name (str): The last name of the User.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
