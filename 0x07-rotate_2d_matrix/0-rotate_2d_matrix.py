#!/usr/bin/python3
"""
    Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
        Given an n x n 2D matrix, rotate it 90 degrees clockwise.

        Do not return anything. The matrix must be edited in-place.
        You can assume the matrix will have 2 dimensions and will not be empty.
    """
    reverse_matrix = matrix[0].copy()
    temp = matrix.copy()

    temp.reverse()
    for position in range(len(temp[0])):
        aux = 0

        for element in temp:
            reverse_matrix[aux] = element[position]
            aux = aux + 1

        matrix[position] = reverse_matrix.copy()
