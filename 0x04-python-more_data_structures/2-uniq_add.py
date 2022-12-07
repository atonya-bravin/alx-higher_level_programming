#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_number_list = []
    total = 0
    for index in range(len(my_list)):
        if my_list[index] in unique_number_list:
            continue
        else:
            unique_number_list.append(my_list[index])
    for number in unique_number_list:
        total += number
    return total
