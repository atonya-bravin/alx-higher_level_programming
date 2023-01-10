#!/usr/bin/python3


"""
    Module tasked to implement a student class
"""


class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        class_dictionary = self.__dict__
        select_dictionary = dict()

        if type(attrs) == list:
            for attribute in attrs:
                if type(attribute) != str:
                    return class_dictionary

                if attribute in class_dictionary:
                    select_dictionary[attribute] = class_dictionary[attribute]

            return select_dictionary
        return class_dictionary
