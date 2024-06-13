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
        return 0

    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op

    return 0
