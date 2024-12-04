import time

from grid_loader import GridLoader
from grid_printer import GridPrinter
from grid import empty_grid


loader = GridLoader("input.txt")
printer = GridPrinter()
printer.clear_console_before_print = True

grid = loader.get_grid()
new_grid = empty_grid(
    grid.height,
    grid.width)

for i in range(grid.height):
    for j in range(grid.width):
        live_neighbours_count = 0
        for k in range(9):
            if k == 4:
                continue
            x = i - 1 + (k // 3)
            y = j - 1 + (k % 3)
            if grid[x % grid.height][y % grid.width].is_alive:
                live_neighbours_count += 1
        grid[i][j].live_neighbours = live_neighbours_count

printer.print_grid_to_console(grid)
total = skips = 0
t = time.time()


for _ in range(10000):
    new_grid = empty_grid(
        grid.height,
        grid.width)

    for i in range(grid.height):
        for j in range(grid.width):
            cell = grid[i][j]
            cell_state = cell.is_alive
            live_neighbours_count = cell.live_neighbours

            total += 1
            if live_neighbours_count < 2:
                skips += 1
                continue

            if cell_state:
                new_cell_state = True if 2 <= live_neighbours_count <= 3 else False
            else:
                new_cell_state = True if live_neighbours_count == 3 else False
            if new_cell_state:
                for k in range(9):
                    if k == 4:
                        continue
                    x = i - 1 + (k // 3)
                    y = j - 1 + (k % 3)
                    new_grid[x % grid.height][y % grid.width].live_neighbours += 1
            new_grid[i][j].is_alive = new_cell_state
    grid = new_grid


print(f"#### end: skips/total = {skips}/{total}, {skips/total:.2%} #### ")
print(f"time: {time.time() - t:.2} s")
printer.print_grid_to_console(grid)
