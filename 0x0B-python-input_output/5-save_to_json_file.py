#!/usr/bin/python3

"""
    Module that is tasked with writing an Object to a text file,
    using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
        writes an object to a text file, using JSON rep
    """

    with open(filename, "w") as myFile:
        myFile.write(json.dumps(my_obj))
