#!/usr/bin/python3
"""city Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City Class
    Class that will hold the information about the city of the user
    Public class attributes:
        - state_id: the id of the state
        - name: name of the city
    """

    state_id = ""
    name = ""
