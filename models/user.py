#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines attributes for the creation user instance
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
