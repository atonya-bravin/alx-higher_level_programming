#!/usr/bin/python3
"""
    Module that is tasked with rep of string as JSON
"""


import json


def from_json_string(my_str):
    """
        returns JSON rep as object(string)
    """

    return json.loads(my_str)
