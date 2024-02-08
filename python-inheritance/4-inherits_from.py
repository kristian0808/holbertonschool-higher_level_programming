#!/usr/bin/python3
"""Write a function that d class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """function Same class or inherit from"""
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
