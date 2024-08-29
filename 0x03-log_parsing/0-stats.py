#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
"""

import sys

total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Prints the current statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_file_size += file_size

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except (IndexError, ValueError):
            continue

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Print statistics when interrupted by CTRL + C
    print_stats()
    raise

print_stats()
