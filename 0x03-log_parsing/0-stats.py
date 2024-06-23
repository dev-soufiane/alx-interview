#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys


def print_status(status_dict, file_size):
    """
    Print total file size and status code counts.

    Args:
        status_dict (dict): Dictionary with status codes and counts.
        file_size (int): Total size of files processed.
    """
    print(f"File size: {file_size}")
    for key in sorted(status_dict.keys()):
        if status_dict[key] != 0:
            print(f"{key}: {status_dict[key]}")


# Initialize counters and status dictionary
status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
               '404': 0, '405': 0, '500': 0}
file_size = 0  # Total file size counter
line_count = 0  # Number of lines read from input

try:
    for line in sys.stdin:
        if line_count != 0 and line_count % 10 == 0:
            # Print metrics every 10 lines
            print_status(status_dict, file_size)

        elem = line.split(" ")  # Split the line by space
        line_count += 1

        try:
            # Get file size from the last element
            file_size += int(elem[-1])
        except ValueError:
            pass  # Ignore non-integer file sizes

        try:
            # Get HTTP status code from the second-to-last element
            if elem[-2] in status_dict.keys():
                status_dict[elem[-2]] += 1
        except IndexError:
            pass  # Handle lines without status code

    print_status(status_dict, file_size)  # Print final metrics

except KeyboardInterrupt:
    print_status(status_dict, file_size)
    raise  # Propagate KeyboardInterrupt
