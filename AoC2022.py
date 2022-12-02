#!/usr/bin/env python3
import AoC2022


def run():
    for day in AoC2022.__all__:
        # Create and run the command that runs this day
        try:
            cmd = f"AoC2022.{day}.run()"
            output = eval(cmd)
        except BaseException as e:
            output = f"ERROR: This day has an error: {type(e).__name__}"

        # Put the result in a nice string
        result = (
            f"======={day} results========\n"
            f"{output}\n"
        )

        # And print the string
        print(result)


if __name__ == "__main__":
    run()
