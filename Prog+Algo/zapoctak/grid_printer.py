import os
from grid import Grid


class GridPrinter:
    live_cell = "@"
    dead_cell = "."

    clear_console_before_print = False

    def print_grid_to_console(self, grid: Grid, spaces=True) -> None:
        out = ""
        spacer = " " if spaces else ""
        for row in grid:
            for cell in row:
                out += self.live_cell if cell.is_alive else self.dead_cell
                out += spacer
            out += "\n"

        if self.clear_console_before_print:
            os.system("cls")
        print(out)

        # out = ""
        # spacer = " " if spaces else ""
        # for row in grid:
        #     for cell in row:
        #         out += str(cell.live_neighbours if cell.live_neighbours else ".")
        #         out += spacer
        #     out += "\n"
        # print(out)
