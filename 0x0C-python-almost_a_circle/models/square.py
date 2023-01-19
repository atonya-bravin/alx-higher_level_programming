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
        my_string = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                      self.y, self.height)
        return my_string

    @property
    def size(self):
        """
            the size getter method
        """

        return self.width

    @size.setter
    def size(self, value):
        """
            the size setter method
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            used to update attributes using
            an unknown number of attributes
        """
        argc = len(args)
        kwargc = len(kwargs)
        valid_args = ['id', 'size', 'x', 'y']

        if (argc > 4):
            argc = 4
        if (argc > 0):
            for args_count in range(argc):
                setattr(self, valid_args[args_count], args[args_count])
        elif (kwargc > 0):
            for key, value in kwargs.items():
                if key in valid_args:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
            returns the dictionary of the square attributes
        """

        return {
                    'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y
                }
