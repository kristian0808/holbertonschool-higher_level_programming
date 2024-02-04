#!/usr/bin/python3

"""
This module contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"

    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix):
            raise TypeError(err1)

    if not \
        all(isinstance(item, (int, float)) for row in matrix for item in row):
            raise TypeError(err1)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(err2)

    if not isinstance(div, (int, float)):
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError(err4)

    return [[round(item / div, 2) for item in row] for row in matrix]
