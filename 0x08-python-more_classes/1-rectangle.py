#!/usr/bin/python

"""
    Module that builds up on module 0-rectangle.py
"""


class Rectangle:
    """
        All built up Rectagle
    """

    @property
    def width(self):
        """
            prints out the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
            sets the width of the rectangle
        """

        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
            prints out the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
            sets the height of the rectangle
        """

        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def __init__(self, width=0, height=0):
        """
            instance instantiation method
        """

        self.width = width
        self.height = height
