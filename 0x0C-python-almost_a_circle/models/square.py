#!/usr/bin/python3

"""
    This is the module that is tasked with creating
    square functionalities
"""


from .rectangle import Rectangle

class Square(Rectangle):
    """
        class used to create square instances
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        my_string = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
        return my_string
