#!/usr/bin/python3
"""amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class:
    - Containing information of the amenity
    Public Class attribute:
        - name: name of the amenity
    """

    name = ""
