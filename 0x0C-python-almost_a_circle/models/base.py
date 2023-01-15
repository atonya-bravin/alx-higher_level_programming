#!/usr/bin/python3

"""
    This is the base mode
"""


class Base():
    """
        The goal of this class is to manage id attribute in all our future
        classes and to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0
    id = None;

    def __init__(self, id=None):
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
