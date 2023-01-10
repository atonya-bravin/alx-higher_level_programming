#!/usr/bin/python3
"""
    Module that is tasked with JSON rep as object(string)
"""


import json


def to_json_string(my_obj):
    """
        returns JSON rep as object(string)
    """

    return json.dumps(my_obj)
