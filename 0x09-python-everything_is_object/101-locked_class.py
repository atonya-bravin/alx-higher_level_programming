#!/usr/bin/python3

"""
    Module with a locked class
"""


class LockedClass(object):
    """
        This class instances can only and only take the property 'first_name'
    """

    __slots__ = 'first_name'
