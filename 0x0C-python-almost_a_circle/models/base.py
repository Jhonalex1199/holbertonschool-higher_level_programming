#!/usr/bin/python3
"""Base class"""
import json
import csv


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
