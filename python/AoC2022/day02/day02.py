#!/usr/bin/env python3.10

import os


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    # return "A Y\nB X\nC Z"

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> list[list[int]]:
    """Divide input into a list of rounds, which in turn is a set of moves"""
    # Explicitly set the type here to avoid the IDE complaining about mixing strings and integers
    rounds: list[list[int | str]] = [move_set.split() for move_set in input_str.splitlines()]
    # Convert to integers for easier comparison. Integer value is also score for move.
    # 1: Rock, 2: Paper, 3: Scissors
    for move_set in rounds:
        move_set[0] = ord(move_set[0]) - 64
        move_set[1] = ord(move_set[1]) - 87

    return rounds


def calculate_score(rounds: list[list[int]]) -> int:
    """Calculate the score for a given set of rounds"""
    total_score = 0
    for move_elf, move_me in rounds:
        # Compare two moves. Returning 0 means elf won, 1 means a draw, 2 means I won.
        # 1,2,3 was chosen for easy point calculation, just multiply it with 3 to get points for this round.
        if move_elf == move_me:
            # A draw
            who_won = 1
        elif move_elf % 3 == (move_me + 1) % 3:
            # Elf won
            who_won = 0
        else:
            # I won
            who_won = 2

        # Add round points and move points to total score
        total_score += who_won * 3 + move_me

    return total_score


def calculate_move(rounds: list[list[int]]) -> list[list[int]]:
    """Interpret the second column of the rounds list as the desired result, set move accordingly."""
    for move_set in rounds:
        if move_set[1] == 1:
            # Must lose
            move_set[1] = (move_set[0] - 2) % 3 + 1
        elif move_set[1] == 2:
            # Must be a draw
            move_set[1] = move_set[0]
        else:
            # Must win
            move_set[1] = move_set[0] % 3 + 1

    return rounds


def run() -> str:
    rounds = process_input(get_input())
    return (
        f"Total score with strategy 1: {calculate_score(rounds)}\n"
        f"Total score with strategy 2: {calculate_score(calculate_move(rounds))}\n"
    )


if __name__ == "__main__":
    print(run())
