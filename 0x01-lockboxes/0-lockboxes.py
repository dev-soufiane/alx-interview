#!/usr/bin/python3
"""
Unlocking Locked Boxes

Given a list of locked boxes with keys,
determine if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened.

    :param boxes: List of lists representing locked boxes and their keys.
    :return: True if all boxes can be opened, else False.
    """
    # Ensure input is a valid list
    if not boxes or type(boxes) is not list:
        return False

    # Initialize list of unlocked boxes
    unlocked_boxes = [0]

    # Iterate through boxes and keys to unlock
    for current_box in unlocked_boxes:
        for key in boxes[current_box]:
            # Check if key can unlock a new box
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    # Check if all boxes are unlocked
    return len(unlocked_boxes) == len(boxes)
