#!/usr/bin/ python3
"""
Island Perimeter
Create a function that returns the perimeter
of the island described in grid:

    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside
    that isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
        Returns the perimeter of the island
    """

    per = 0
    for x in range(len(grid)):

        for y in range(len(grid[x])):
            if grid[x][y] == 1:

                # Go Up
                if (x-1 < 0) or grid[x - 1][y] == 0:
                    per = per + 1

                # Go Left
                if (y - 1 < 0) or grid[x][y - 1] == 0:
                    per = per + 1

                # Go Right
                if (y + 1 >= len(grid[x])) or grid[x][y + 1] == 0:
                    per = per + 1

                if (x + 1 >= len(grid)) or grid[x + 1][y] == 0:
                    per = per + 1

    return per
