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


def process_input(input_str: str) -> list[list[int]]:
    """Divide input into a list of rounds, which in turn is a set of moves"""
    rounds = [move_set.split() for move_set in input_str.splitlines()]
    # Convert to integers for easier comparison. Integer value is also score for move.
    for move_set in rounds:
        move_set[0] = int(ord(move_set[0]) - 64)
        move_set[1] = int(ord(move_set[1]) - 87)

    return rounds


def calculate_score(rounds: list[list[int]]) -> int:
    """Calculate the score for a given set of rounds"""
    score = 0
    for move_elf, move_me in rounds:
        score += get_move_score(move_elf, move_me)

    return score


def compare_moves(left: int, right: int) -> int:
    """Compare two moves. Returning 0 means left won, 1 means right won, 2 means a draw"""
    if left:
        pass


def get_move_score(left: str, right: str) -> int:
    """Get the score for a single move"""
    pass


def run() -> str:
    rounds = process_input('A Y\nB X\nC Z')
    return f"Total score: {calculate_score(rounds)}"


if __name__ == "__main__":
    print(run())
