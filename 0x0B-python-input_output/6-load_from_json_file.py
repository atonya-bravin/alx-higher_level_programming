#!/usr/bin/python3

"""
    Module that is tasked with getting JSON and conveting it to an Object
"""

import json


def load_from_json_file(filename):
    """
        gets JSON and convets it to an Object
    """

    with open(filename, "r") as myFile:
        return json.loads(myFile.read())
