#!/usr/bin/python3

"""
    Function that determine if all the boxes can be opened.
    In n number of locked boxes, each box is numbered sequentially
    from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ Method that compare the total len of the boxes.
    Compare them according his number and position. """

    for key_value in range(1, len(boxes) - 1):

        exist = False

        for position_box in range(len(boxes)):

            exist = (key_value in boxes[position_box]
                     and key_value != position_box)

            if exist:
                break

        if exist is False:
            return exist

    return True
