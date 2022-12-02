#!/usr/bin/env python3
import AoC2022
import pkgutil


def run():
    # Find all subpackages in AoC2022
    days = pkgutil.iter_modules(AoC2022.__path__)

    for day in days:
        # Skip this module if it is not a day
        if not day.name.startswith('day'):
            continue

        # Create and run the command that runs this day
        cmd = f"AoC2022.{day.name}.run()"
        output = eval(cmd)

        # Put the result in a nice string
        result = (
            f"======={day.name} results========\n"
            f"{output}\n"
        )

        # And print the string
        print(result)


if __name__ == "__main__":
    run()
