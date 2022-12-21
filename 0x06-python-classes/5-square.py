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

    @property
    def size(self):
        """Retrives the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the size of the square (setter)"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square"""

        return (self.__size ** 2)

    def my_print(self):
        """prints the square using the # character"""

        if (self.__size > 0):
            for counter in range(self.__size):
                for counter in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
