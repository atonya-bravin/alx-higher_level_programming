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

        return (self.__width * self.__height)

    def perimeter(self):
        """
            returns the perimeter of our rectangle
        """

        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = ((self.__height * 2) + (self.__width * 2))

        return perimeter

    def __str__(self):
        """
            returns a string of # forming a rectangle
        """

        rectangle_string = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle_string

        for height_drawer in range(self.__height):
            for width_drawer in range(self.__width):
                rectangle_string = rectangle_string + "#"
            if height_drawer < self.__height - 1:
                rectangle_string = rectangle_string + "\n"
        return rectangle_string

    def __repr__(self):
        """
            Returns a string representation of the rectangle instance
        """

        width_eval = str(eval('self.width'))
        height_eval = str(eval('self.height'))

        return 'Rectangle(' + width_eval + ', ' + height_eval + ')'

    def __init__(self, width=0, height=0):
        """
            instance instantiation method
        """

        self.__width = width
        self.__height = height
