#!/usr/bin/python3

"""
    Module that contains functions that implemets the division
    of all elements of a mtrix
"""


def matrix_divided(matrix, div):
    """
        function that implements the division of all elements
        of a matrix with the div value
    """

    results_list = []
    new_matrix = []

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_str = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_str)

    for index in range(len(matrix)):
        if type(matrix[index]) is not list:
            raise TypeError(err_str)
        else:
            expected_row_size = len(matrix[index])

        if len(matrix[index - 1]) != expected_row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in matrix[index]:
            if type(element) not in (int, float):
                raise TypeError(err_str)

            result = round((element / div), 2)

            results_list.append(result)

        new_matrix.append(results_list.copy())
        del results_list[:]
    return(new_matrix)
