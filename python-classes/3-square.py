#!/usr/bin/python3

""" created a class Square and added a private attribute "size" """


class Square:
    """dding attribute size as a private instance"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
