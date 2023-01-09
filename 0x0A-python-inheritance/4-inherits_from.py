#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
        inherits_from: checks if object is an instance of
        a class that inherited

        Args
        ****
        @obj: the object to check for
        @a_class: the class to counter from

        Return
        ******
        Returns True if the object is an instance of a class that inherited
        Otherwise False
    """
    is_instance = isinstance(obj, a_class)
    is_subclass = issubclass(a_class, obj.__class__) is False

    if (is_instance and is_subclass):
        return True
    return False
