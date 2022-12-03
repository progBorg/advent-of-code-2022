#!/usr/bin/env python3

import os


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    prac = (
        "vJrwpWtwJgWrhcsFMMfFFhFp\n"
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n"
        "PmmdzqPrVvPwwTWBwg\n"
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n"
        "ttgJtRGJQctTZtZT\n"
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    )
    # return prac

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> list[list[str]]:
    rucksacks = []
    for sack in input_str.splitlines():
        half = len(sack) // 2 # Assuming length is even
        rucksacks.append([sack[0:half], sack[-half:]])

    return rucksacks


def get_sum_of_priorities(rucksacks: list[list[str]]) -> int:
    total_sum = 0
    for sack in rucksacks:
        if len(sack[0]) > 0:
            for item in sack[0]:
                if item in sack[1]:
                    # Assuming there is always a duplicate item
                    break

            total_sum += get_priority(item)

    return total_sum


def get_sum_of_badges(rucksacks: list[list[str]]) -> int:
    total_sum = 0
    group_size = 3
    elfs = [''] * 3

    for i in range(0, len(rucksacks), group_size):
        for elf in range(group_size):
            elfs[elf] = rucksacks[i+elf][0] + rucksacks[i+elf][1]

        for item in elfs[0]:
            is_badge = True
            for elf in elfs[1:]:
                if item not in elf:
                    is_badge = False
                    break

            if is_badge is True:
                total_sum += get_priority(item)
                break

    return total_sum


def get_priority(item: str) -> int:
    return ord(item) - 38 if ord(item) <= 91 else ord(item) - 96


def run() -> str:
    sacks = process_input(get_input())
    return (
        f"Sum of duplicate item's priorities: {get_sum_of_priorities(sacks)}\n"
        f"Sum of badge priorities: {get_sum_of_badges(sacks)}\n"
    )


if __name__ == "__main__":
    print(run())
