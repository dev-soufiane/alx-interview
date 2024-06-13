#!/usr/bin/env python3
"""
Minimum operations required to achieve a specific character count.
"""


def minOperations(n):
    """
    Calculates the fewest operations to reach n characters.

    Args:
        n (int): Target number of characters.

    Returns:
        int: Minimum number of operations required.
    """
    if n <= 1:
        return n

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
