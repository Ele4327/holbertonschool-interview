#!/usr/bin/python3

"""
    Function that returns a list of lists of integers representing the
    Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """Function take a number, n, and return a list of lists of integers"""
    if n <= 0:
        return[]

    triangle_index = [[1]]
    while len(triangle_index) != n:

        adjacent = triangle_index[-1]
        actual = [1]

        for x in range(len(adjacent) - 1):
            actual.append(adjacent[x] + adjacent[x + 1])
        actual.append(1)
        triangle_index.append(actual)

    return triangle_index
