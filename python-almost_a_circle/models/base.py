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
        """
        Class method to save json represantation of
        object files
        """

        with open(f"{cls.__name__}.json", "w+") as file_js:
            if list_objs is None:
                file_js.write(json.dumps([]))
                return
            list_of_dictionaries = []
            for objs in list_objs:
                if issubclass(objs.__class__, Base):
                    list_of_dictionaries.append(objs.to_dictionary())
            file_js.write(Base.to_json_string(list_of_dictionaries))
