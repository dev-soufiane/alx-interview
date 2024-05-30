#!/usr/bin/python3
"""Pascal's Triangle """


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    n (int): Number of rows to generate.

    Returns:
    list of lists: Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]  # first element is always 1
        if triangle:  # if triangle has elements (not the first row)
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # last element is always 1
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Prints the Pascal's triangle.

    Args:
    triangle (list of lists): Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))


if __name__ == "__main__":

    print_triangle(pascal_triangle(5))
