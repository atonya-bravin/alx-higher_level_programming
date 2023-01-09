#!/usr/bin/python3
"""
    Module that prints a sorted list
"""


class MyList(list):
    """
        the class that is used to hold the list data
    """

    def print_sorted(self):
        """
            the method that prints the sorted list
        """

        if issubclass(MyList, list):
            print(sorted(self))
