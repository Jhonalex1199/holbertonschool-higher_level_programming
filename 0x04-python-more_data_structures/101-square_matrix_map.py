#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix2 = []
    for i in matrix:
        matrix2.append(list(map(lambda i: i ** 2, i)))
    return matrix2
