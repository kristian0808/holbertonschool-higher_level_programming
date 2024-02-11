#!/usr/bin/python3
"""a function that writes in a file"""


def write_file(filename="", text=""):
    """reads a file and overwrite"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
