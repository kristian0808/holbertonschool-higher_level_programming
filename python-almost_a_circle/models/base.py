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
        """ omeeeeeeeee """
        if cls is None:
            cls = "Rectangle"
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        serialized_data = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(serialized_data)

        with open(filename, "w") as file:
            file.write(json_string)
