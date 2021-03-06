#!/usr/bin/python3
"""a documentation of my modules"""


class Square:
    """a documentation of my class"""

    def __init__(self, size=0):

        """ private attribute : .__size """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
