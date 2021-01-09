#!/usr/bin/python3
"""Divide a matrix"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""
    if not check_matrix(matrix):
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")
    for i in matrix:
        if len(i) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(x/div, 2) for x in j] for j in matrix]


def check_matrix(matrix):
    if not isinstance(matrix, list):
        return False
    for i in matrix:
        if type(i) is not list:
            return False
        if any(not isinstance(y, (int, float)) for y in i):
            return False
    return True
