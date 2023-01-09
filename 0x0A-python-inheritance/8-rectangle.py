#!/usr/bin/python3

"""
    Module building up on 5-base_geometry.py
"""


class BaseGeometry():
    """
        a class that contains
          area() method to raise an exception
          integer_validator() method to validate values
    """

    def area(self):
        """
            function that raises an exception with the message;
            <<area() is not implemented>>
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            integer_validator - validates the value
        """

        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))

        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
        a class that initializes rectangles
    """

    def __init__(self, width, height):
        """
            object initializer
        """

        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
