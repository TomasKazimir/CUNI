import copy
import itertools
from typing import List


class Sudoku:
    def __init__(self, board: List[List[int]]) -> None:
        self.puzzle = tuple(tuple(row) for row in board)
        self.solution = board
        self.solutions = []

    def is_solved(self) -> bool:
        for row in self.solution:
            if len(set(row)) != 9:
                return False

        for j in range(9):
            col = [self.solution[i][j] for i in range(9)]
            if len(set(col)) != 9:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [self.solution[i + k][j + l]
                       for k in range(3)
                       for l in range(3)]
                if len(set(box)) != 9:
                    return False

        return True

    def is_valid_placement(self, n: int, i: int, j: int) -> bool:
        # row
        if n in self.solution[i]: return False
        # column
        for col in range(9):
            if n == self.solution[col][j]:
                return False
        # box
        i = 3 * (i // 3)
        j = 3 * (j // 3)
        for k in range(3):
            for l in range(3):
                if n == self.solution[i + k][j + l]:
                    return False
        return True

    def solution_found(self):
        self.solutions.append(copy.deepcopy(self.solution))
        print("  >>> Solution found <<<")
        # print(len(self.solutions))
        print(*self.solution, sep="\n")
        input("\nPress Enter to continue...\n")

    def solve(self):
        if self.is_solved():
            return self.solution

        tried = list(itertools.chain.from_iterable(self.puzzle))

        I = 0
        backtrack = False
        while 0 <= I <= 80:
            # check if cell at index I is fixed
            if self.puzzle[I // 9][I % 9] != 0:
                if backtrack:
                    I -= 1
                    continue
                else:
                    if I == 80:
                        self.solution_found()
                        I -= 1
                        continue
                    I += 1
                    continue

            if backtrack:
                if tried[I] == 9:  # all numbers have been tried already
                    tried[I] = 0
                    self.solution[I // 9][I % 9] = 0
                    I -= 1
                    continue
                else:
                    backtrack = False

            for i in range(tried[I] + 1, 10):
                if self.is_valid_placement(i, I // 9, I % 9):
                    self.solution[I // 9][I % 9] = i
                    tried[I] = i
                    I += 1
                    break
            else:
                backtrack = True
                tried[I] = 0
                self.solution[I // 9][I % 9] = 0
                I -= 1

            if I == 0:
                if backtrack:
                    print("All solutions found")
                    break
            if I == 81:
                self.solution_found()
                I -= 1

        if len(self.solutions):
            return self.solutions
        else:
            return None


b = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 0],
    [0, 0, 5, 0, 1, 0, 0, 0, 0],
]  # 3 solutions
# b = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]
b = Sudoku(b)
print(b.solve())
