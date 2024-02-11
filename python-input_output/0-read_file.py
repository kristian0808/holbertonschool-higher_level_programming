#!/usr/bin/python3
"""a function that reads a file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
