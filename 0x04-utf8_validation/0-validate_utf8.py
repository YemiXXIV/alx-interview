#!/usr/bin/python3
"""
Module for UTF-8 Validation.
"""


def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.
    """

    number_of_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7

        if number_of_bytes == 0:
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1

            if number_of_bytes == 0:
                continue

            if number_of_bytes == 1 or number_of_bytes > 4:
                return False

        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        number_of_bytes -= 1

    return number_of_bytes == 0
