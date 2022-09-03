#!/usr/bin/python3
from models.base_model import BaseModel
"""Define the Place Class that inherits from BaseModel."""


class Place(BaseModel):
    """Represents a Place.
    Attr:
        city_id (str): The id of the City
        user_id (str): The id of the User
        name (str): The name of the Place
        description (str): The description of the Place
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The Maximum number of Guests
        price_by_night (int): Price of Rooms per Night
        latitude (float) : The latitude of the Place
        longitude (float): The longitude of the Place
        amenity_ids (list): The list of Amenity id
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
