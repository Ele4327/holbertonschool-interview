#!/usr/bin/python3

"""
Method that calculates the fewest number of operations needed.
n -> number of operations to reach
Returns a integer
"""


def minOperations(n: int) -> int:

    x = 2

    if n <= 1:
        return (0)

    total_value = 0

    while (n != 1):
        if n % x == 0:
            n = n / x
            total_value = total_value + x
        else:
            x = x + 1

    return(total_value)
