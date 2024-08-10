#!/usr/bin/python3
"""
Algo for lock boxes
"""


def canUnlockAll(boxes):
    """
    lock boxes algorithm
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]
    holder = []

    while stack:
        checker = stack.pop()
        holder.append(checker)
        visited[checker] = True
        for key in boxes[checker]:
            if key < n and key not in stack and key not in holder:
                stack.append(key)
    return all(visited)
