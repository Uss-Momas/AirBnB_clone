#!/usr/bin/python3
"""state module"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class:
    - Containing information of the state of the user.
    Class variable:
        - name: name of the state
    """

    name = ""
