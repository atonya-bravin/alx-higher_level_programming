#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for outter_idx in range(len(matrix)):
            for inner_idx in range(len(matrix[outter_idx])):
                print("{:d}".format(matrix[outter_idx][inner_idx]), end=" ")
            print()
