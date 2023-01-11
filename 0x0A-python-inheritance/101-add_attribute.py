#!/usr/bin/python3

"""
    Module that is tasked with checking whether an attribute
    can be added to a class and does that if possible
"""


def add_attribute(self, key, value):
    """
        adds an attribute to a class if possible else raises TypeError
    """

    if (type(self) != str):
        setattr(self, key, value)
    else:
        raise TypeError("can't add new attribute")
