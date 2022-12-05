#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validate_tuple(tuple_a)
    tuple_b = validate_tuple(tuple_b)

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))


def validate_tuple(test_tuple=()):
    if len(test_tuple) < 2:
        if len(test_tuple) == 1:
            test_tuple = (test_tuple[0], 0)
        elif len(test_tuple) == 0:
            test_tuple = (0, 0)
        elif len(test_tuple) > 2:
            test_tuple = (test_tuple[0], test_tuple[1])

    return test_tuple
