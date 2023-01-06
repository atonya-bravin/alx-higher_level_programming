#!/usr/bin/python3

"""
    Module that builds up on module 0-rectangle.py
"""


class Rectangle:
    """
        All built up Rectagle
    """

    number_of_instances = 0
    print_symbol = "#"

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
                rectangle_string = rectangle_string + str(self.print_symbol)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            returns the biggest rectangle based on the area of the rectangles
        """

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
            that returns a new Rectangle instance with width == height == size
        """

        if type(size) != int:
            raise TypeError("height must be an integer")

        if size < 0:
            raise ValueError("height must be >= 0")
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """
            instance instantiation method
        """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __del__(self):
        """
            called anytime an instance is deleted using the del method
        """

        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
