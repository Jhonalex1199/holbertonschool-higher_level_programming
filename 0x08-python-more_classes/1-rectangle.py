#!/usr/bin/python3
"""Rectangle module."""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = value
        self.__height = value

        if type(width) is not int:
            raise TypeError("size must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")

        if type(height) is not int:
            raise TypeError("size must be an integer")
        if height < 0:
            raise ValueError("size must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(width) is not int:
            raise TypeError("size must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(height) is not int:
            raise TypeError("size must be an integer")
        if height < 0:
            raise ValueError("size must be >= 0")
