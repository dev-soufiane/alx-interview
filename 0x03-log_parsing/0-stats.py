#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""
import sys


def print_status(status_dict, size):
    """
    Prints file size and status code counts.

    Args:
        status_dict (dict): Dictionary of status codes.
        size (int): Total file size.
    """
    print(f"File size: {size}")
    for key in sorted(status_dict.keys()):
        if status_dict[key] != 0:
            print(f"{key}: {status_dict[key]}")


def main():
    """
    Main function to process stdin and compute metrics.
    """
    status_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                   '404': 0, '405': 0, '500': 0}

    file_size = 0  # Total file size
    line_count = 0  # Number of lines read

    try:
        for line in sys.stdin:
            line = line.strip()
            if line_count != 0 and line_count % 10 == 0:
                print_status(status_dict, file_size)

            elements = line.split()
            if len(elements) >= 9:
                status_code = elements[-2]
                try:
                    file_size += int(elements[-1])
                    if status_code in status_dict:
                        status_dict[status_code] += 1
                except ValueError:
                    pass  # Ignore non-integer file sizes

            line_count += 1

        print_status(status_dict, file_size)  # Final metrics

    except KeyboardInterrupt:
        print_status(status_dict, file_size)
        raise


if __name__ == "__main__":
    main()
