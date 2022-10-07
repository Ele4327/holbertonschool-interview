#!/usr/bin/python3
"""
    Prime Game
"""


def isWinner(x, nums):
    """
        where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
        You cannot import any packages in this task
    """
    if (x < 1):
        return None
    number = 0
    for round in range(x):
        number = number ^ (nums[round % len(nums)])

    if number > 0:
        return "Ben"
    else:
        return "Maria"
