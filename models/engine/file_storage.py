#!/usr/bin/python3
"""
Module to store file
"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """
        obj_name = obj.__class__.__name__
        key = f"{obj_name}.{obj.id}"
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the dictionary of all objects
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        all_objs = FileStorage.__objects
        obj_dict = {}

        for key, obj in all_objs.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

