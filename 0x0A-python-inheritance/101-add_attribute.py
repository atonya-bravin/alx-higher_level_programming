#!/usr/bin/python3

"""
    Module that is tasked with checking whether an attribute
    can be added to a class and does that if possible
"""


def add_attribute(self, key, value):
    try:
        setattr(self, key, value)
    except Exception:
        raise TypeError("can't add new attribute")
