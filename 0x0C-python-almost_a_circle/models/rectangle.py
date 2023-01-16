#!/usr/bin/python3

"""
    Module that is tasked with the creation of a rectangle
"""

from .base import Base

class Rectangle(Base):
    """
        This class is a build up of the Base class
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.setter_validator(height, 'height')
        self.setter_validator(width, 'width')
        self.setter_validator(x, 'x')
        self.setter_validator(y, 'y')

        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    def setter_validator(self, value, param):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(param))
        if param in ('height', 'width') and value <= 0:
            raise ValueError("{} must be > 0".format(param))
        if param in ('x', 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(param))


    @property
    def width():
        return __width

    @property
    def height():
        return __height

    @property
    def x():
        return x

    @property
    def y():
        return y

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self,height):
        self.__height = height

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def area(self):
        return (self.__width*self.__height)

    def display(self):
        for y_index in range(self.__y):
            print()
        for outer_index in range(self.__height):
            for x_index in range(self.__x):
                print(" ", end="")
            for inner_index in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        my_string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return my_string

    def update(self, *args):
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        argument_count = len(args)

        if (argument_count > 5):
            argument_count = 5

        if (argument_count > 0):
            for argc in range(argument_count):
                setattr(self, modif_attrs[argc], args[argc])
