#!/usr/bin/python3

"""
    Contains methods that work with people names
"""


def say_my_name(first_name, last_name=""):
    """
        function that concatinates  first and second names
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("second_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
