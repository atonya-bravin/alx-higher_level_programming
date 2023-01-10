#!/usr/bin/python3

"""
    Module that uses File handling
"""


def read_file(filename=""):
    """
        file that reads and prints file content
    """

    with open(filename, "r", encoding="utf-8") as myFile:
        for fileLine_content in myFile:
            print(fileLine_content, end="")
