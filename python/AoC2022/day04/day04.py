#!/usr/bin/env python3

import os
import re


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    prac = (
        "2-4,6-8\n"
        "2-3,4-5\n"
        "5-7,7-9\n"
        "2-8,3-7\n"
        "6-6,4-6\n"
        "2-6,4-8\n"
    )
    # return prac

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> list[list[tuple[int, int]]]:
    sections = []
    for pair in input_str.splitlines():
        section = re.split('[,-]', pair)
        sections.append([(int(section[0]), int(section[1])), (int(section[2]), int(section[3]))])

    return sections


def get_fully_contained_sum(sections: list[list[tuple[int, int]]]) -> int:
    total_sum = 0
    for pair in sections:
        if is_contained(pair[0], pair[1]) or is_contained(pair[1], pair[0]):
            total_sum += 1

    return total_sum


def is_contained(outer: tuple[int, int], inner: tuple[int, int]) -> bool:
    return outer[0] <= inner[0] and outer[1] >= inner[1]


def get_partially_contained_sum(sections: list[list[tuple[int, int]]]) -> int:
    total_sum = 0
    for pair in sections:
        if has_overlap(pair[0], pair[1]):
            total_sum += 1

    return total_sum


def has_overlap(left: tuple[int, int], right: tuple[int, int]) -> bool:
    """https://stackoverflow.com/questions/3269434/whats-the-most-efficient-way-to-test-if-two-ranges-overlap#3269471"""
    return left[0] <= right[1] and right[0] <= left[1]


def run() -> str:
    sections = process_input(get_input())
    return (
        f"Sum of fully contained sections: {get_fully_contained_sum(sections)}\n"
        f"Sum of partially contained sections: {get_partially_contained_sum(sections)}\n"
    )


if __name__ == "__main__":
    print(run())
