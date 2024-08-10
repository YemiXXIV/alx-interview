#!/usr/bin/python3
"""
Python pascal triangle module
"""


def pascal_triangle(n):
    """
    module for pascal triangle
    """
    if n > 0:
        triangle = [[1]]
        if n > 1:
            for i in range(1, n):
                temp_triangle = [1]
                for j in range(1, i):
                    temp_triangle.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                temp_triangle.append(1)
                triangle.append(temp_triangle)
        return triangle
    else:
        return []
