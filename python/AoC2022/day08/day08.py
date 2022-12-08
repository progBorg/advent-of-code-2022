#!/usr/bin/env python3

import os
import numpy as np


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    prac = (
        "30373\n"
        "25512\n"
        "65332\n"
        "33549\n"
        "35390\n"
    )
    # return prac

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> np.ndarray:
    lines = input_str.splitlines()
    grid = np.array([int(c) for c in lines[0]])
    for line in lines[1:]:
        grid = np.vstack((grid, [int(c) for c in line]))

    return grid


def get_num_visible_trees(grid: np.ndarray) -> int:
    left = mark_visible_trees_ltr(grid)
    right = np.fliplr(mark_visible_trees_ltr(np.fliplr(grid)))
    top = mark_visible_trees_ltr(grid.T).T
    bottom = np.fliplr(mark_visible_trees_ltr(np.fliplr(grid.T))).T

    return int(np.sum(left | right | top | bottom))


def mark_visible_trees_ltr(grid: np.ndarray) -> np.ndarray:
    """Mark hidden trees as 0, visible as 1 from left to right"""
    marked_grid = grid.copy()
    rows, cols = marked_grid.shape
    for row in range(rows):
        height = -1
        for col in range(cols):
            if marked_grid[row, col] > height:
                height = marked_grid[row, col]
                marked_grid[row, col] = 1
            else:
                marked_grid[row, col] = 0

    return marked_grid


def get_highest_scenic_score(grid: np.ndarray) -> int:
    left = mark_distance_tree_ltr(grid)
    right = np.fliplr(mark_distance_tree_ltr(np.fliplr(grid)))
    top = mark_distance_tree_ltr(grid.T).T
    bottom = np.fliplr(mark_distance_tree_ltr(np.fliplr(grid.T))).T

    return np.max(left * right * top * bottom)


def mark_distance_tree_ltr(grid: np.ndarray) -> np.ndarray:
    """Mark a tree's viewing distance looking from left to right"""
    marked_grid = grid.copy()
    rows, cols = marked_grid.shape
    for row in range(rows):
        dist = 0
        for col in range(cols):
            if dist <= 0:
                # Find next taller tree
                dist = np.nonzero(
                    marked_grid[row, col+1:] >= marked_grid[row, col]
                )[0]
                dist = np.min(dist) + 1 if len(dist) > 0 else cols - col - 1
            marked_grid[row, col] = dist
            dist -= 1

    return marked_grid


def run() -> str:
    grid = process_input(get_input())
    return (
        f"Number of visible trees: {get_num_visible_trees(grid)}\n"
        f"Best scenic score: {get_highest_scenic_score(grid)}\n"
    )


if __name__ == "__main__":
    print(run())
