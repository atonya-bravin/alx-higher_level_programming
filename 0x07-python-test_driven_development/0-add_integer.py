#!/usr/bin/python3

"""
    Module that adds two integers or floats
"""


def add_integer(a, b=98):
    """
        add-integer: adds two integers or floats and returns the result
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
