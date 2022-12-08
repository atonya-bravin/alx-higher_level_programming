#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    product_dictionary = {}
    for key, value in a_dictionary.items():
        product_dictionary[key] = value * 2

    return product_dictionary
