#!/usr/bin/python3
"""
Define the base model for the entire project.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base model class with id, creation, and update timestamps.
    """

    def __init__(self):
        """
        Initialize the class and create the needed public attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Update the update time.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Convert the instance to a dictionary.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic

    def __str__(self):
        """
        Create the string representation of the class.
        """
        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.__dict__}"
