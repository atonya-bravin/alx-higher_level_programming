#!/usr/bin/python3

"""
    Module tasked with overloading of "==" and "!="
"""


class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if (self.value == other):
            return False
        return True

    def __ne__(self, other):
        if (self.value != other):
            return False
        return True
