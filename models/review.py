#!/usr/bin/python3
"""review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    Public class attributes:
        - place_id
        - user_id
        - text
    """

    place_id = ""
    user_id = ""
    text = ""
