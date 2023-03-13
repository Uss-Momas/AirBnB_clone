#!/usr/bin/python3
"""user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class
    Public variables:
        email - user email
        password - user password
        first_name - user first name
        last_name - user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
