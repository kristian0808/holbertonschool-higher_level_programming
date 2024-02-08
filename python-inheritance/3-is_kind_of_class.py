#!/usr/bin/python3
"""Write a function that red class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """function Same class or inherit from"""
    if isinstance(obj, a_class):
        return True
    return False
