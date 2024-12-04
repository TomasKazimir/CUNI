from typing import List
from cell import Cell


class Grid:
    def __init__(self, grid: List[List[Cell]]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def __getitem__(self, item: int):
        return self.grid[item]

def empty_grid(height: int, width: int) -> Grid:
    return Grid(
        [[Cell(False) for _ in range(width)]
         for _ in range(height)]
    )
