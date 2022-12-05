#!/usr/bin/env python3

import os
import re


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    prac = (
        "    [D]\n"
        "[N] [C]\n"
        "[Z] [M] [P]\n"
        " 1   2   3\n" 
        "\n"
        "move 1 from 2 to 1\n"
        "move 3 from 1 to 3\n"
        "move 2 from 2 to 1\n"
        "move 1 from 1 to 2\n"
    )
    # return prac

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> tuple[dict[int, list[str]], list[tuple[int, int, int]]]:
    crates_str, inst_str = input_str.split('\n\n')

    # Parse crates
    crates_str = crates_str.splitlines()[::-1]  # Mirror order
    crates: dict[int, list[str]] = {}
    for crate_num in range(1, len(crates_str[0]), 4):
        stack_num: int = int(crates_str[0][crate_num])
        crates[stack_num] = []

        for stack in crates_str[1:]:
            # Make sure stack indexing does not get out of bounds
            if len(stack) > crate_num:
                crate: str = stack[crate_num]
                # Only add a crate if there actually is one
                if crate.isalpha():
                    crates[stack_num].append(crate)

    # Parse instructions
    instructions: list[tuple[int, int, int]] = []
    for inst in inst_str.splitlines():
        p = re.split("move|from|to|$", inst)
        instructions.append((int(p[1]), int(p[2]), int(p[3])))

    return crates, instructions


def find_top_crates_CM9000(crates: dict[int, list[str]], instructions: list[tuple[int, int, int]]) -> str:
    # Make a copy of the crate stack, so we don't edit the original
    crates_copy = {}
    for num, stack in crates.items():
        crates_copy[num] = stack.copy()

    for inst in instructions:
        for i in range(inst[0]):
            crates_copy[inst[2]].append(crates_copy[inst[1]].pop())

    top_crates = ''.join([str(v[-1]) for v in crates.values()])
    return top_crates


def find_top_crates_CM9001(crates: dict[int, list[str]], instructions: list[tuple[int, int, int]]) -> str:
    # Make a copy of the crate stack, so we don't edit the original
    crates_copy = {}
    for num, stack in crates.items():
        crates_copy[num] = stack.copy()

    for inst in instructions:
        crates_copy[inst[2]].extend(crates_copy[inst[1]][-inst[0]:])
        del crates_copy[inst[1]][-inst[0]:]

    top_crates = ''.join([str(v[-1]) for v in crates_copy.values()])
    return top_crates


def run() -> str:
    crates, instructions = process_input(get_input())
    return (
        f"Top crates with individual movement: {find_top_crates_CM9000(crates, instructions)}\n"
        f"Top crates with stack movement: {find_top_crates_CM9001(crates, instructions)}\n"
    )


if __name__ == "__main__":
    print(run())
