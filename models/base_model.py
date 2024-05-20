#!/usr/bin/python3
"""
Define the base model for the entire project.
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    Base model class with id, creation, and update timestamps.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class and create the needed public attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in {"updated_at", "created_at"}:
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            
        models.storage.new(self)

    def save(self):
        """
        Update the update time.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Convert the instance to a dictionary.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()

        return dic

