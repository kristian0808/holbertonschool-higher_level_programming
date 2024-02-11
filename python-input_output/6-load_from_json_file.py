#!/usr/bin/python3
"""Write a function that writes an Object to
a text file, using a JSON representation:"""
import json


def load_from_json_file(filename):
    """Return JSON"""
    with open(filename, "r") as file:
        for line in file:
            return json.loads(line)
