#!/usr/bin/python3

"""
    Module that checks whether an object is an instance of an object
    or that of its parrent
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class: checks whether the object is an instance
        of a class or that of its parent

        Args
        ****
        @obj: the object to check validity for
        @a_class: the class to check as type

        Return
        ******
        Returns True if object is an instance of a_class
        otherwise returns False
    """

    return isinstance(obj, a_class)
