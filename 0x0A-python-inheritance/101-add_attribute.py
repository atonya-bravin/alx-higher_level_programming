#!/usr/bin/python3

"""
    Module that is tasked with checking whether an attribute
    can be added to a class and does that if possible
"""


def add_attribute(self, key, value):
    """
        adds an attribute to a class if possible else raises TypeError
    """

    if (type(self) not in [int, str, list]):
        if (key not in self.__slots__):
            raise TypeError("can't add new attribute")
        setattr(self, key, value)
        print(self.__slots__)
    else:
        raise TypeError("can't add new attribute")
