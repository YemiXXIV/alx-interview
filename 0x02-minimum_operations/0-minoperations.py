#!/usr/bin/python3
"""
This module provides a function to calculate the
minimum number of operations needed to achieve exactly
`n` 'H' characters in a text file using only "Copy All"
and "Paste" operations.
"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed
    to result in exactly n 'H' characters in the file.
    """

    # If n is less than or equal to 1, no operations can be performed
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor

        factor += 1

    return operations
