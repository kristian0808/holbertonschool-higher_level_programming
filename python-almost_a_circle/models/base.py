#!/usr/bin/python3
"""Write the first class Base"""
import json
import os.path


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json string of a list list dictionaries"""
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        if cls is None:
            cls = "Rectangle"
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        serialized_data = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(serialized_data)

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is not None and len(json_string) > 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            def_class = cls(4)
        else:
            def_class = cls(5, 3)
        def_class.update(**dictionary)
        return def_class

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            lines_dict = cls.from_json_string(file.read())
        return [cls.create(**dict_instance) for dict_instance in lines_dict]
