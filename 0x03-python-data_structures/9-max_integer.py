#!/usr/bin/python3
def max_integer(my_list=[]):
    max_integer = 0
    if len(my_list) != 0:
        for index in range(len(my_list)):
            if my_list[index] > max_integer:
                max_integer = my_list[index]
    else:
        return None
    return max_integer
