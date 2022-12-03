#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for outer_idx in range(len(matrix)):
            for inner_idx in range(len(matrix[outer_idx])):
                if inner_idx == (len(matrix[outer_idx]) - 1):
                    print("{:d}".format(matrix[outer_idx][inner_idx]), end="")
                else:
                    print("{:d}".format(matrix[outer_idx][inner_idx]), end=" ")
            print()
