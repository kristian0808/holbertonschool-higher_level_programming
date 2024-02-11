#!/usr/bin/python3
"""Write a class Square that inherits
    from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class"""

    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        return self.__size**2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
