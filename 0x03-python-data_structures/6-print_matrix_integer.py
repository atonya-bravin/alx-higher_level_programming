#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    cariage_return = "\n"
    if matrix:
        for outter_index in range(len(matrix)):
            for inner_index in range(len(matrix[outter_index])):
                print("{:d}".format(matrix[outter_index][inner_index]), end=" ")
            print("{}".foramt(cariage_return))
