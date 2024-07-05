#!/usr/bin/python3
"""
N Queens Puzzle Solver
Usage: nqueens N

The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.

This program solves the N queens problem and
prints every possible solution to the problem.

Arguments:
N: An integer greater or equal to 4 representing the size
of the chessboard and the number of queens.

If the user called the program with the wrong number of arguments,
it prints "Usage: nqueens N" and exits with status 1.
If N is not an integer, it prints "N must be a number" and exits with status 1.
If N is smaller than 4, it prints "N must be at least 4"
and exits with status 1.
"""
import sys


def is_safe(board, r, c, N):
    for i in range(r):
        if board[i] == c or board[i] == c - r + i or board[i] == c + r - i:
            return False
    return True


def nqueens(N, board, row):
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens(N, board, row + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens(N, board, 0)
