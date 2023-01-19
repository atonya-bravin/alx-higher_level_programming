#!/usr/bin/python3

"""
    This is the base mode
"""
import json


class Base():
    """
        The goal of this class is to manage id attribute in all our future
        classes and to avoid duplicating the same code
        (by extension, same bugs)
    """

    __nb_objects = 0
    id = None

    def __init__(self, id=None):
        """
            initialization method
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            returns a string representation of the dict passed to it
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            saves the json to string rep to a file
        """

        my_list = []

        file_name = "{}.json".format(cls.__name__)
        with open(file_name, "w") as file_des:
            if list_objs is None:
                return file_des.write(cls.to_json_string(None))
            for elem in list_objs:
                my_list.append(elem.to_dictionary())

            return file_des.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
            returns a list from string
        """

        if json_string is None:
            return []
        else:
            return json.loads(json_string)
