#!/usr/bin/python3

"""
    Module that uses File handling
"""


def read_file(filename=""):
    """
        file that reads and prints file content
    """

    with open(filename, "r") as myFile:
        file_content = myFile.read()

    print(file_content)
