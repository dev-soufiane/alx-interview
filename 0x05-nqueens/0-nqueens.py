#!/usr/bin/python3
"""
N queens problem
"""

import sys


def safe_position(board, row, col):
    """
    Check safety for placing queen at (row, col) on board.
    """
    board_size = len(board)

    # Check row horizontally
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper diagonal left
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check lower diagonal left
    r, c = row, col
    while r < board_size and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True


def SolveNqueens(board, col, solutions):
    """
    Recursively solve NQueens problem column-wise.

    Args:
        board (list): Current board state.
        col (int): Current column to place queen.
        solutions (list): List to store found solutions.

    Returns:
        bool: True if solution found, else False.
    """
    board_size = len(board)

    if col == board_size:
        # Found solution, convert board to coordinates and add to solutions
        solution = []
        for r in range(board_size):
            for c in range(board_size):
                if board[r][c] == 1:
                    solution.append([r, c])
        solutions.append(solution)
        return True

    found = False
    for r in range(board_size):
        if safe_position(board, r, col):
            # Place queen and recurse
            board[r][col] = 1
            found = SolveNqueens(board, col + 1, solutions) or found
            # Backtrack
            board[r][col] = 0

    return found


def NQueens(n):
    """
    Solve and print all solutions for N Queens problem.

    Args:
        n (int): Size of chessboard and number of queens.

    Returns: None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    SolveNqueens(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        NQueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
