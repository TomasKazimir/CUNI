import sys
import os

from typing import List
from time import sleep

LIFE = "O"
DEATH = " "


class Board:
    def __init__(self, values: List[List]):
        self.r = len(values)
        self.c = len(values[0])
        self.values = values

    def __repr__(self):
        return "\n".join([" ".join(str(_) for _ in row) for row in self.values])


def read_input() -> tuple:
    input_data = []
    for line in sys.stdin.readlines():
        input_data.append(line.rstrip())

    c, r = (int(_) for _ in input_data[0].split())
    t = int(input_data[1])
    ### CHANGE
    # return c, r, t, input_data[2:]
    input_data = input_data[2:]
    return len(input_data[0]), len(input_data), t, input_data


def zero_board(r: int, c: int, x: str | int = 0) -> Board:
    return Board([[x for _ in range(c)] for _ in range(r)])


def pprint(x, sep_len: int = 40) -> None:
    print("=" * sep_len)
    print(x)


def life_or_death(state: str, n: int) -> str:
    if state == LIFE:
        if 2 <= n <= 3:
            return LIFE
        return DEATH
    return LIFE if n == 3 else DEATH


if __name__ == "__main__":
    col_len, row_len, n_of_sims, data = read_input()

    board = zero_board(row_len, col_len, DEATH)
    for i in range(row_len):
        for j in range(col_len):
            board.values[i][j] = DEATH if data[i][j] == "." else LIFE

    for _ in range(n_of_sims):
        new_board = zero_board(row_len, col_len, DEATH)
        for i in range(row_len):
            for j in range(col_len):
                neighbours = 0 if board.values[i][j] == DEATH else -1
                cell_state = board.values[i][j]
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        neighbours += 0 if board.values[(i + k) % row_len][(j + l) % col_len] == DEATH else 1
                new_board.values[i][j] = life_or_death(cell_state, neighbours)
        board.values = new_board.values
        os.system("cls")
        pprint(board, sep_len=col_len)
        sleep(0.05)
