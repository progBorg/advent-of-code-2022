#!/usr/bin/env python3

import os


def get_input() -> str:
    """Read out input as a single string"""
    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str):
    """Divide input into a list of elves, which in turn is a list of calories (integers)"""
    pass


def run() -> str:
    raise NotImplementedError("Not yet implemented")


if __name__ == "__main__":
    print(run())
