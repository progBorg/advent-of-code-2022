#!/usr/bin/env python3

import os
import re

CD = 0
LS = 1

def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    prac = (
        "$ cd /\n"
        "$ ls\n"
        "dir a\n"
        "14848514 b.txt\n"
        "8504156 c.dat\n"
        "dir d\n"
        "$ cd a\n"
        "$ ls\n"
        "dir e\n"
        "29116 f\n"
        "2557 g\n"
        "62596 h.lst\n"
        "$ cd e\n"
        "$ ls\n"
        "584 i\n"
        "$ cd ..\n"
        "$ cd ..\n"
        "$ cd d\n"
        "$ ls\n"
        "4060174 j\n"
        "8033020 d.log\n"
        "5626152 d.ext\n"
        "7214296 k\n"
    )
    return prac

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> list[list[int, any]]:
    commands = []
    for single_command in re.split("\$ ", input_str):
        lines = single_command.splitlines()
        cmd = lines[0].split() if len(lines) > 0 else ['']
        if cmd[0] == 'cd':
            command = [CD, cmd[1]]
        elif cmd[0] == 'ls':
            command = [LS, lines[1:]]
        else:
            # No known command, so also don't append to list
            continue

        commands.append(command)

    return commands


def find_directory_size(commands: dict[str, str]) -> int:
    return -1


def run() -> str:
    commands = process_input(get_input())
    return (
        f"Total size of directories: {find_directory_size(commands)}\n"
        # f"Start of first message is at character: {find_first_marker(charstream, 14)}\n"
    )


if __name__ == "__main__":
    print(run())
