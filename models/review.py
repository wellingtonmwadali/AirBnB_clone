#!/usr/bin/python3
"""module for the Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """Implementation the Review model"""
    place_id = ""
    user_id = ""
    text = ""
