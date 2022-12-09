#!/usr/bin/env python3

import os
import numpy as np


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    prac = (
        "R 4\n"
        "U 4\n"
        "L 3\n"
        "D 1\n"
        "R 4\n"
        "D 1\n"
        "L 5\n"
        "R 2\n"
    )
    prac2 = (
        "R 5\n"
        "U 8\n"
        "L 8\n"
        "D 3\n"
        "R 17\n"
        "D 10\n"
        "L 25\n"
        "U 20\n"
    )
    # return prac2

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> list[list[str, int]]:
    # Trying out oneliners for a change
    return [[tup[0], int(tup[1])] for tup in [line.split() for line in input_str.splitlines()]]


def find_visited_tail_positions(head_motions: list[list[str, int]]) -> int:
    h_pos = np.array([0, 0])  # Startpoint is origin
    t_pos = np.array([0, 0])
    t_pos_visited = {(0, 0)}  # Startpoint also counts as visited
    max_dist = np.linalg.norm((1, 1))  # Maximum allowed distance between head and tail (one diagonal)
    for dir, dis in head_motions:
        dir = get_direction(dir)

        for s in range(dis):
            h_pos += dir
            t_pos, _ = update_position(h_pos, t_pos, dir, max_dist)

            # Add new position to visited list
            # set makes sure every position occurs only once
            t_pos_visited.add(tuple(t_pos))

    return len(t_pos_visited)


def update_position(
        front_knot: np.ndarray, back_knot: np.ndarray, dir: tuple[int, int], max_dist: float
) -> tuple[np.ndarray, tuple[int, int]]:
    """Update the position of back_knot based on the location of front_knot.
    dir is the direction front_knot moved
    """
    if np.linalg.norm(front_knot - back_knot) > max_dist:
        # Update tail position if too far away
        new_back_knot = back_knot + dir

        if np.linalg.norm(new_back_knot - back_knot) != max_dist:
            # Only execute when there is no fully diagonal movement
            if dir[0] != 0:  # L-R movement
                new_back_knot[1] = front_knot[1]
            else:  # U-D movement
                new_back_knot[0] = front_knot[0]
    else:
        new_back_knot = back_knot

    # Return the new position back_knot moved to, and the movement it made to get there
    return new_back_knot, tuple(new_back_knot - back_knot)


def get_direction(dir_str: str) -> tuple[int, int]:
    if dir_str == 'R':
        dir = (1, 0)
    elif dir_str == 'L':
        dir = (-1, 0)
    elif dir_str == 'U':
        dir = (0, 1)
    elif dir_str == 'D':
        dir = (0, -1)
    else:
        raise RuntimeError(f"No valid direction specified: {dir_str}")

    return dir


def find_visited_tail_positions_long(head_motions: list[list[str, int]], rope_length: int = 10, plot: bool = False) -> int:
    pos = [np.array((0, 0)) for i in range(rope_length)]  # Keep track of each knot's position
    t_pos_visited = {(0, 0)}  # Startpoint also counts as visited
    max_dist = np.sqrt(2)  # Maximum allowed distance between head and tail (one diagonal)
    for dir, dis in head_motions:
        dir = get_direction(dir)

        for s in range(dis):
            pos[0] += dir  # Update head position
            prev_dir = dir
            # Propagate through rope
            for k in range(len(pos) - 1):
                # Contents of this for-loop plagiarised from https://github.com/emielsteerneman/AoC-2022/blob/main/day9/day9.py
                Hx, Hy = pos[k]
                Tx, Ty = pos[k + 1]

                # Calculate euclidean distance
                dx, dy = Tx - Hx, Ty - Hy
                distance = np.linalg.norm((dx, dy))

                # Basically, if distance further than sqrt(2)
                if 2 <= distance:
                    # Normalize distance vector, round it, add it to upstream knot
                    Tx, Ty = Hx + round(dx / distance), Hy + round(dy / distance)
                    pos[k + 1] = [Tx, Ty]

            # Add new position to visited list
            # set makes sure every position occurs only once
            t_pos_visited.add(tuple(pos[-1]))

    if plot:
        plot_visited(t_pos_visited)

    return len(t_pos_visited)


def plot_visited(pos: set[tuple[int, int]]):
    x_list = [tup[0] for tup in pos]
    y_list = [tup[1] for tup in pos]
    origin = (-min(x_list), -min(y_list))
    grid = np.full((-min(x_list)+max(x_list) + 1, -min(y_list)+max(y_list) + 1), '.')

    for x, y in pos:
        grid[x+origin[0], y+origin[1]] = '#'

    grid[origin] = 's'

    for row in grid:
        print(''.join(row))


def run() -> str:
    head_motions = process_input(get_input())
    return (
        f"Number of positions visited by the tail of rope length 2: {find_visited_tail_positions(head_motions)}\n"
        f"Number of positions visited by the tail of rope length 10: {find_visited_tail_positions_long(head_motions)}\n"
    )


if __name__ == "__main__":
    print(run())
