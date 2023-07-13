#!/usr/bin/python3
"""model for the Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Implemenatations of the Place model

    Args:
        city_id (str): The id of the city.
        user_id (str): The id of the user.
        name (str): The  place's name.
        description (str): The place's description.
        number_rooms (int): The place number of rooms.
        number_bathrooms (int): The place's max number of bedrooms.
        max_guest (int): The  place max number of guests.
        price_by_night (int): The place price per night.
        latitude (float): The  place's latitude
        longitude (float): The place's longitude.
        amenity_ids (list): A list of Amenity ids.
    """
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
    amenity_ids = []
