#!/usr/bin/python3

"""
    Module that contains functions that implemets the division of all elements of a mtrix
"""


def matrix_divided(matrix, div):
    """
        function that implements the division of all element s of a matrix with the div value
    """

    results_list = []
    new_matrix = []

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    expected_row_size = len(matrix[0])

    for index in range(len(matrix)):
        if type(matrix[index]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        if len(matrix[index]) != expected_row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in matrix[index]:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = round((element / div), 2)

            results_list.append(result)

        new_matrix.append(results_list.copy())
        del results_list[:]
        
    return(new_matrix)
