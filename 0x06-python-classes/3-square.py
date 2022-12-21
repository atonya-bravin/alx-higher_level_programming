#!/usr/bin/python3

"""Square class
   Creation of an empty class Square that defines a square
"""


class Square:
    """
        This class defines a Private instance attribute: size
    """

    def __init__(self, size=0):
        """initializer function"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of a square"""

        return (self.__size ** 2)
