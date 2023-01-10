#!/usr/bin/python3

"""
    Module tasked to add arguments from the command line into a list
"""


from os import path
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


def work_magic(fileName):
    args = sys.argv[1:]
    jsonfile = "add_item.json"
    try:
        my_list = load(jsonfile)
    except FileNotFoundError:
        save(args, jsonfile)
    else:
        my_list.extend(args)
        save(my_list, jsonfile)


work_magic("add_item.json")
