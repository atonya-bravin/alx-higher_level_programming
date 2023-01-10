#!/usr/bin/python3

"""
    Module tasked to add arguments from the command line into a list
"""


from os import path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def work_magic(fileName):

    if path.exists('add_item.json'):
        with open(fileName, "r") as myFile:
            my_list = load_from_json_file(fileName)

        for arg_index in range(1, len(sys.argv)):
            my_list.append(sys.argv[arg_index])

        with open(fileName, "w") as myFile:
            save_to_json_file(my_list, fileName)
    else:
        my_list = []
        with open(fileName, "w") as myFile:
            save_to_json_file(my_list, fileName)


work_magic("add_item.json")
