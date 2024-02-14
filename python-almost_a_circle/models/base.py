#!/usr/bin/python3
""" base class """
import json


class Base:
    """base"""

    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(list_dicts))
