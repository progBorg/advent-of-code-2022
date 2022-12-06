#!/usr/bin/env python3

import os
import re


def get_input() -> str:
    """Read out input as a single string"""
    # Practice input
    # return "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

    # Get absolute path to input file
    fname = 'input.txt'
    this_file = os.path.abspath(__file__)
    this_dir = os.path.dirname(this_file)
    input_file = os.path.join(this_dir, fname)

    with open(input_file) as f:
        return f.read()


def process_input(input_str: str) -> str:
    return input_str


def find_first_marker(charstream: str, packet_size: int) -> int:
    for start, end in enumerate(range(packet_size, len(charstream))):
        # set() condenses a list to contain only unique values
        if len(set(charstream[start:end])) == packet_size:
            return end

    return -1


def run() -> str:
    charstream = process_input(get_input())
    return (
        f"Start of first packet is at character: {find_first_marker(charstream, 4)}\n"
        f"Start of first message is at character: {find_first_marker(charstream, 14)}\n"
    )


if __name__ == "__main__":
    print(run())
