#!/usr/bin/python3
"""
Module 0-minoperations
Calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations, or 0 if n is impossible.
    """
    # Impossible to achieve n chars if n is less than 2
    if n < 2:
        return 0

    ops = 0
    factor = 2

    while n > 1:
        # While n is divisible by the current factor (e.g., 2)
        while n % factor == 0:
            # Add the factor to operations (Copy + Paste...Paste)
            ops += factor
            # Divide n to reduce it
            n //= factor
        # Move to the next possible factor
        factor += 1

    return ops
