#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Checks if list of ints is valid UTF-8 encoding

    Args:
        data (list): List of ints representing data bytes.

    Returns:
        bool: True if valid UTF-8, False otherwise.
    """
    nbrs_of_bytez = 0  # Num of bytes in current UTF-8 char

    for nbr in data:
        # Convert number to binary representation
        binary_rep = format(nbr, '#010b')[-8:]

        if nbrs_of_bytez == 0:  # Start processing new UTF-8 char
            for i in binary_rep:
                if i == '0':
                    break
                nbrs_of_bytez += 1

            if nbrs_of_bytez == 0:  # Invalid start of char
                continue

            # Invalid num of bytes for char
            if nbrs_of_bytez == 1 or nbrs_of_bytez > 4:
                return False
        else:
            # Check if byte is continuation byte
            if not binary_rep.startswith('10'):
                return False
        nbrs_of_bytez -= 1

    return nbrs_of_bytez == 0
