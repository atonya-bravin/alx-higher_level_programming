#!/usr/lib/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for outter_index in range(len(matrix)):
        product_matrix = []
        for inner_index in range(len(matrix[outter_index])):           
            inner_matrix = matrix[outter_index][inner_index]
            product_matrix.append(inner_matrix ** 2)
        new_matrix.append(product_matrix)
    return new_matrix
