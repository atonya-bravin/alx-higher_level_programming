#!/usr/bin/python3

"""
    Module that is functioned to check validity of an object
"""


def is_same_class(obj, a_class):
    """
        is_same_class: checks whether an object is an instance of
        a specific class

        args
        ****
        @obj: the object to check validity for
        @a_class: the class that instantiates the object

        Returns
        ********
        True if is an instance of the class
        otherwise returns false
    """

    if (type(obj) == a_class):
        return True
    return False
