#!/usr/bin/env python3
"""
Rotate 2D Matrix Clockwise

This script rotates a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)

    # Step 1: Perform matrix transpose
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        # Reverse the elements in the current row
        matrix[i] = matrix[i][::-1]
