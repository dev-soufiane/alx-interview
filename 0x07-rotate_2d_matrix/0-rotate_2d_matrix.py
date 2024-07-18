#!/usr/bin/python3
"""
Rotate 2D Matrix Clockwise

This script rotates a 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    """
    n = len(matrix)


    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for i in range(n):
        # Use slicing to reverse the row
        matrix[i] = matrix[i][::-1]
