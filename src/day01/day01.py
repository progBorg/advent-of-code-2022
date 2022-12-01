#!/usr/bin/env python3

def get_input() -> str:
    """Read out input as a single string"""
    with open('input.txt') as f:
        return f.read()


def process_input(input_str: str) -> list[list[int]]:
    """Divide input into a list of elves, which in turn is a list of calories (integers)"""
    all_calories = input_str.split('\n\n')
    calories = []
    for elf in all_calories:
        calories.append([eval(i) for i in elf.strip('\n').split('\n')])
    return calories


def find_highest_sum(calories: list[list[int]]) -> int:
    """Find the single highest sum in the list of elves"""
    max_sum = 0
    for elf in calories:
        max_sum = sum(elf) if sum(elf) > max_sum else max_sum
    return max_sum


def find_three_highest_sum(calories: list[list[int]]) -> int:
    """Find the three highest sums in the list of elves"""
    max_sums = [0, 0, 0] # Ordered as highest value first
    for elf in calories:
        for i, s in enumerate(max_sums):
            if sum(elf) > s:
                # If higher than the current max_sum, then put new value in its place. Values get shifted to the right,
                # after which the last one can be popped of to get back to three values again.
                max_sums.insert(i, sum(elf))
                max_sums.pop()
                break
    return sum(max_sums)


if __name__ == "__main__":
    print("Highest sum of calories:")
    print(find_highest_sum(
        process_input(get_input())
    ))

    print("Three highest sums of calories combined:")
    print(find_three_highest_sum(
        process_input(get_input())
    ))
