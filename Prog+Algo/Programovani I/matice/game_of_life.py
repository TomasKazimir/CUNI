import sys
import os

from typing import List, Tuple
from time import sleep

LIFE  = "@"     # ∎
DEATH = " "     # ·
NUMBER_OF_SIMULATED_CYCLES = 10000
PAUSE = .05

class Board:
    def __init__(self, values: List[List]):
        self.r = len(values)
        self.c = len(values[0])
        self.values = values

    def __repr__(self):
        out = "#" + "#".join([" ".join(str(_) for _ in row) for row in self.values])
        splits = out.count("#")
        for i in range(splits):
            out = out.replace("#", f"|\n{i:3}|", 1)
        return out[2:] + "|"


def read_input() -> Tuple[int, int, int, list]:
    input_data = []
    for line in sys.stdin.readlines():
        input_data.append(line.rstrip().replace(" ", ""))
    input_data.pop()
    return len(input_data[0]), len(input_data), input_data


def zero_board(r: int, c: int, x: str | int = 0) -> Board:
    return Board([[x for _ in range(c)] for _ in range(r)])


def pprint(x, sep_len: int = 40) -> None:
    print("   " + "__" * sep_len + "_")
    print(x)
    print("   " + "‾‾" * sep_len + "‾")


def life_or_death(state: str, n: int) -> str:
    if state == LIFE:
        if 2 <= n <= 3:
            return LIFE
        return DEATH
    return LIFE if n == 3 else DEATH


if __name__ == "__main__":
    col_len, row_len, data = read_input()

    board = zero_board(row_len, col_len, DEATH)
    for i in range(row_len):
        for j in range(col_len):
            board.values[i][j] = DEATH if data[i][j] == "." else LIFE

    for t in range(NUMBER_OF_SIMULATED_CYCLES):
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
        print(t+1)
        sleep(PAUSE)
