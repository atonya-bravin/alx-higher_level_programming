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
        """
            initialization method
        """

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
        """
            validates a value if the value is a correct value
            to be used in the application
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(param))
        if value <= 0 and param in ('height', 'width'):
            raise ValueError("{} must be > 0".format(param))
        if value < 0 and param in ('x', 'y'):
            raise ValueError("{} must be >= 0".format(param))

    @property
    def width(self):
        """
            the width getter method
        """

        return self.__width

    @property
    def height(self):
        """
            the hight getter method
        """

        return self.__height

    @property
    def x(self):
        """
            the X getter method
        """

        return self.__x

    @property
    def y(self):
        """
            the y getter method
        """

        return self.__y

    @width.setter
    def width(self, width):
        """
            the width setter method
        """

        self.setter_validator(width, 'width')
        self.__width = width

    @height.setter
    def height(self, height):
        """
            the height setter method
        """

        self.setter_validator(height, 'height')
        self.__height = height

    @x.setter
    def x(self, x):
        """
            the x setter method
        """

        self.setter_validator(x, 'x')
        self.__x = x

    @y.setter
    def y(self, y):
        """
            the y setter method
        """

        self.setter_validator(y, 'y')
        self.__y = y

    def area(self):
        """
            finds and returns the area of a rect
        """

        return (self.__width*self.__height)

    def display(self):
        """
            displays a rect using the '#' character
        """

        for y_index in range(self.__y):
            print()
        for outer_index in range(self.__height):
            for x_index in range(self.__x):
                print(" ", end="")
            for inner_index in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
            function overloading
        """

        my_string = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                            self.y,
                                                            self.width,
                                                            self.height)
        return my_string

    def update(self, *args, **kwargs):
        """
            uses passed in parameters to updarte class attributes
        """

        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        argument_count = len(args)
        key_count = len(kwargs)

        if (argument_count > 5):
            argument_count = 5

        if (argument_count > 0):
            for argc in range(argument_count):
                setattr(self, modif_attrs[argc], args[argc])
        elif (key_count > 0):
            for (key, value) in kwargs.items():
                if key in modif_attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
            returns the object as a dictionary
        """
        return {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                }
