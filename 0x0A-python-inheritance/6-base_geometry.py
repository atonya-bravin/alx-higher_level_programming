#!/usr/bin/python3

"""
    Module building up on 5-base_geometry.py
"""


class BaseGeometry():
    """
        a class that contains area() method to raise an exception
    """

    def area(self):
        """
            function that raises an exception with the message;
            <<area() is not implemented>>
        """

        raise Exception("area() is not implemented")
