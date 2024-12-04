import sys
from copy import deepcopy


def can_place_rook(board, i, j):
    if i < 0 or i >= n or j < 0 or j >= n:
        # print("placement outside of board", i, j)
        return False
    if board[i][j] != ".":
        # print("placement on occupied square", i, j)
        return False
    if "#" in board[i]:
        # print("a rook is present in this rank", i, j)
        return False
    if "#" in [board[x][j] for x in range(n)]:
        # print("a rook is present in this file", i, j)
        return False
    return True


def _place_rook(board, i, j):
    if not can_place_rook(board, i, j):  # we can place no more rooks - invalid
        return 0
    elif i == n-1:  # this is the last rank and a rook CAN be placed here
        board[i][j] = "#"
        # print(*board, sep="\n", end="\n\n")
        return 1
    board_copy = deepcopy(board)
    board_copy[i][j] = "#"
    c = 0
    for k in range(n):
        c += _place_rook(board_copy, i+1, k)
    return c


def place_rook(board):
    p = 0
    for j in range(n):
        # print(f"Place 1st rook on 0,{j}")
        if can_place_rook(board, 0, j):
            p += _place_rook(board, 0, j)
        # print(f"END 0,{j}")
    return p


if __name__ == "__main__":
    n = (int(input()))
    board = []

    # load board from stdin
    for line in sys.stdin:
        board += [[char for char in line.strip()]]

    # counter for total number of valid solutions
    valid_rook_constellations = 0

    print(place_rook(board))



