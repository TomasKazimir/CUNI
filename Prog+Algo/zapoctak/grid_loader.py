from cell import Cell
from grid import Grid


class GridLoader:

    def __init__(self, filename: str):
        self.filename = filename
        self.grid = None
        self.load_grid()

    def load_grid(self) -> None:
        grid = []
        with open(self.filename, 'r') as f:
            for line in f:
                grid.append([Cell(False) if char == "."
                             else Cell(True)
                             for char in line.strip()])
        self.grid = Grid(grid)

    def get_grid(self) -> Grid:
        return self.grid
