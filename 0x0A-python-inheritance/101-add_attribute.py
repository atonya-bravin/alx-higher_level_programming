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
        setattr(self, key, value)
        """
        if (key in self.__slots__):
            raise TypeError("can't add new attribute")
            """
    else:
        raise TypeError("can't add new attribute")
