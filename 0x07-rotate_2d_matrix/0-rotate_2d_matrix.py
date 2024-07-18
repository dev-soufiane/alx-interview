#!/usr/bin/env python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list of list): The matrix to be rotated in-place.

    Returns:
        None. The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    # Example usage:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    rotate_2d_matrix(matrix)

    print("\nMatrix after 90 degree clockwise rotation:")
    for row in matrix:
        print(row)
