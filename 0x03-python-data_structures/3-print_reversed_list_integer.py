#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for index in range(1, len(my_list)):
        print("{}".format(my_list[(index * (-1))]))
    print("{}".format(my_list[len(my_list) * (-1)]))