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

    """getter method"""
    @property
    def size(self):
        return self.__size

    """setter method"""
    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """function that return the curret square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size is 0:
            return print()
        for i in range(self.__size):
            for a in range(self.__size):
                print('#', end="")
            print()
