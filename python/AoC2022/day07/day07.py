#!/usr/bin/env python3

import os
import re

CD: int = 0
LS: int = 1
DIR: int = -1

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
    # return prac

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
            contents = []
            for node in lines[1:]:
                node_type, *name = node.split()
                if node_type == 'dir':
                    node_type = DIR
                contents.append([int(node_type), ' '.join(name)])

            command = [LS, contents]
        else:
            # No known command, so also don't append to list
            continue

        commands.append(command)

    return commands


def find_fs_size(commands: list[list[int, any]], max_size: int = -1) -> tuple[int, int]:
    """Return cumulative sum of directory sizes, and total filesystem size"""
    fs = create_filesystem_structure(commands)
    pwd = fs
    pwd_parents = []
    cum_fs_size = 0
    pwd_parent_key = []
    dir_size = 0
    while isinstance(fs, dict):
        # Find a directory entry in current directory
        for key, node in pwd.items():
            if isinstance(node, dict):
                # If this node is a directory, enter it and start again
                pwd_parents.append(pwd)
                pwd = node
                pwd_parent_key.append(key)
                break

        else:
            # Run this if no directories were found (no break was issued)
            dir_size = sum(pwd.values())
            pwd = pwd_parents.pop()
            if pwd_parent_key[-1] == '/':
                fs = dir_size
            else:
                pwd[pwd_parent_key.pop()] = dir_size

            if max_size < 0 or dir_size < max_size:
                cum_fs_size += dir_size

    # The last dir_size value is the size of /, that is the size of the entire filesystem
    return cum_fs_size, dir_size


def create_filesystem_structure(commands: list[list[int, any]]) -> dict:
    fs = {'/': {}}
    pwd = fs
    pwd_parents = []
    for cmd in commands:
        if cmd[0] == CD:
            if cmd[1] == '..':
                pwd = pwd_parents.pop()
            else:
                # Everything is passed by reference, so updating values in pwd also updates fs
                pwd_parents.append(pwd)
                pwd = pwd[cmd[1]]
        elif cmd[0] == LS:
            for node in cmd[1]:
                if node[0] == DIR:
                    pwd[node[1]] = {}
                else:
                    pwd[node[1]] = node[0]

    return fs


def find_directory_for_deletion(commands: list[list[int, any]], required_space: int) -> str:
    fs = create_filesystem_structure(commands)
    device_size = 70000000
    _, fs_size = find_fs_size(commands)
    needed_space = required_space - (device_size - fs_size)
    if needed_space <= 0:
        # No space needs to be freed, so don't return any directory
        return ''

    pwd = fs
    pwd_parents = []
    pwd_parent_key = []
    del_dir_size = fs_size
    while isinstance(fs, dict):
        # Find a directory entry in current directory
        for key, node in pwd.items():
            if isinstance(node, dict):
                # If this node is a directory, enter it and start again
                pwd_parents.append(pwd)
                pwd = node
                pwd_parent_key.append(key)
                break

        else:
            # Run this if no directories were found (no break was issued)
            dir_size = sum(pwd.values())
            pwd = pwd_parents.pop()
            if pwd_parent_key[-1] == '/':
                fs = dir_size
            else:
                pwd[pwd_parent_key.pop()] = dir_size

            if needed_space < dir_size < del_dir_size:
                del_dir_size = dir_size

    return del_dir_size


def run() -> str:
    commands = process_input(get_input())
    max_size = 100000
    required_space = 30000000
    return (
        f"Total size of directories: {find_fs_size(commands, max_size)[0]}\n"
        f"Size of smallest directory for deletion: {find_directory_for_deletion(commands, required_space)}\n"
    )


if __name__ == "__main__":
    print(run())
