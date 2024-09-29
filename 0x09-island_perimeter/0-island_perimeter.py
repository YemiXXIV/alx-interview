#!/usr/bin/python3
"""
island perimeter module
"""


def island_perimeter(grid):
    """
    island perimeter module
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if c + 1 < cols and grid[r][c + 1] == 1:
                    perimeter -= 2

                if r + 1 < rows and grid[r + 1][c] == 1:
                    perimeter -= 2

    return perimeter
