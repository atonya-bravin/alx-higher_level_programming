#!/usr/bin/python3

"""
    Module that facilitates writting into a file
"""


def write_file(filename="", text=""):
    """
        writes text into a file
    """

    with open(filename, "w", encoding="UTF8") as myFile:
        return myFile.write(text)
