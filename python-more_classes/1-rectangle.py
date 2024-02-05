#!/usr/bin/python3
""" created a class named rectangle """


class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=")
        self.__height = value

