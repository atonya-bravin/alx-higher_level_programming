#!/usr/bin/python3

"""
    Module containing function to print square using # character
"""


def print_square(size):
    """
        Function that prints a square with the character #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if ((type(size) is float) and (size < 0)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for rows in range(size):
        for columns in range(size):
            print("#", end="")

        print()


