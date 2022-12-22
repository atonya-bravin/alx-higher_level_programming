#!/usr/bin/ptyhon3

def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    for index in range(x):
        try:
            if type(my_list[index]) is int and num_printed != x:
                print("{:d}".format(my_list[index]), end="")
                num_printed += 1
        except TypeError:
            continue

    print()
    return num_printed
