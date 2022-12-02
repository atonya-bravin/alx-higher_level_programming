#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    logic_list = []
    for index in range(len(my_list)):
        if (my_list[index] % 2) == 0:
            logic_list.append(True)
        else:
            logic_list.append(False)
    return logic_list
