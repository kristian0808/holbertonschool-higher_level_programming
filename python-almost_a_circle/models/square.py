#!/usr/bin/python3
"""Write the first class Base"""
from .rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update class that assigns an argument"""
        arg_list = ["id", "size", "x", "y"]
        for arg_name, arg_value in zip(arg_list, args):
            setattr(self, arg_name, arg_value)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """dictionary"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Overwrite str square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
