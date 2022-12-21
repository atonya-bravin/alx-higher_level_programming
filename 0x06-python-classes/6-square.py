#!/usr/bin/python3

"""Square class
   Creation of an empty class Square that defines a square
"""


class Square:
    """
        This class defines a Private instance attribute: size
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializer function"""

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0])) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[1])) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrives the size of the square"""

        return (self.__size)

    @property
    def position(self):
        """Retrives the positionof the square"""

        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[0])) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(position[1])) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
                if (self.__position[0] >= 0 and self.__position[1] >= 0):
                    for space_counter in range(self.__position[0]):
                        print(" ", end="")
                for counter in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
