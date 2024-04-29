#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents a file storage engine."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary of objects."""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objs = json.load(file)
                self.__objects = {k: eval(v['__class__'])(**v) for k, v in objs.items()}
        except FileNotFoundError:
            pass

    def get(self, cls, id):
        """Retrieve an object from the dictionary by its class and id."""
        key = "{}.{}".format(cls, id)
        return self.__objects.get(key)

    def count(self, cls=None):
        """Count the number of objects in the dictionary."""
        if cls:
            return len([obj for obj in self.__objects.values() if isinstance(obj, cls)])
        else:
            return len(self.__objects)
