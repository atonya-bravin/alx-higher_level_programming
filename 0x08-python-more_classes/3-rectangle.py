#!/usr/bin/python3

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

    def area(self):
        """
            returns the area of our rectangle
        """

        return (self.width * self.height)

    def perimeter(self):
        """
            returns the perimeter of our rectangle
        """

        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = ((self.height * 2) + (self.width * 2))

        return perimeter

    def __str__(self):
        """
            returns a string of # forming a rectangle
        """

        rectangle_string = ""

        if self.width == 0 or self.height == 0:
            return rectangle_string

        for height_drawer in range(self.height):
            for width_drawer in range(self.width):
                rectangle_string = rectangle_string + "#"
            rectangle_string = rectangle_string + "\n"
        return rectangle_string

    def __print__(self):
        print(_str__(self))

    def __init__(self, width=0, height=0):
        """
            instance instantiation method
        """

        self.width = width
        self.height = height
