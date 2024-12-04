import os
import sys
from time import sleep
from typing import Tuple

type Maze = list[list[str]]
type Vector = tuple[int, int]


# region functions

def load_maze_from_stdin() -> Tuple[int, Maze]:
    out = []
    m = int(input())  # number of moves
    for line in sys.stdin.readlines():
        out.append(
            [char for char in line.strip()]
        )
    return m, out


def is_accessible(maze: Maze, pos: Vector) -> bool:
    if maze[pos[0]][pos[1]] == '.':
        return True
    return False


def get_beasts_position_and_state(maze: Maze) -> Tuple[Vector, str]:
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in "><v^":
                return (i, j), maze[i][j]
    assert False, "There is no beast"


def add_vectors(v1: Vector,
                v2: Vector) -> Vector:
    return v1[0] + v2[0], v1[1] + v2[1]


def rotate_vector(v: Vector,
                  angle: str) -> Vector:
    if angle == "right":
        return v[1], -v[0]
    elif angle == "left":
        return -v[1], v[0]
    else:
        assert False, f"Invalid angle {angle}"


def print_maze(maze: Maze) -> None:
    m = ["".join(row) for row in maze]
    os.system("cls")
    print(*m, sep="\n")
    print()
    sleep(0.1)


# endregion


if __name__ == "__main__":
    # dicts for converting between heading symbols and corresponding vectors
    beast_to_heading = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
    heading_to_beast = dict((v, k) for k, v in beast_to_heading.items())

    t, maze = load_maze_from_stdin()

    position, beast = get_beasts_position_and_state(maze)
    heading = beast_to_heading[beast]
    while t >= 1:
        if is_accessible(maze, add_vectors(position, rotate_vector(heading, "right"))):  # beast can go right
            # turn the beast to the right
            heading = rotate_vector(heading, "right")

            # draw beast's new heading
            maze[position[0]][position[1]] = heading_to_beast[heading]
            print_maze(maze)
            t -= 1

            # draw beast on his new position
            maze[position[0]][position[1]] = "."  # remove beast from current position
            position = add_vectors(position, heading)  # his new position
            maze[position[0]][position[1]] = heading_to_beast[heading]

        elif is_accessible(maze, add_vectors(position, heading)):  # beast can go straight
            # delete beast from his current position
            maze[position[0]][position[1]] = "."

            # new position of the beast
            position = add_vectors(position, heading)

            # draw beast on his new position
            maze[position[0]][position[1]] = heading_to_beast[heading]

        else:  # there's a wall in front of the beast, he must turn left
            # turn the beast to the left
            heading = rotate_vector(heading, "left")

            # draw beast's new heading
            maze[position[0]][position[1]] = heading_to_beast[heading]

        if t >= 1:
            print_maze(maze)
        t -= 1
