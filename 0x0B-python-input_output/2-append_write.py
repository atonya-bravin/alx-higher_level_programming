#!/usr/bin/python3

"""
    Module that facilitates writting to the end of a file
"""


def append_write(filename="", text=""):
    """
        appends text into a file
    """

    with open(filename, "a", encoding="UTF8") as myFile:
        return myFile.write(text)
