#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        end = ""
        for a in i:
            print("{:s}{:d}".format(end, a), end="")
            end = " "
        print()
