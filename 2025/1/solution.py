# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import os

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))


def part_one() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    password = 0
    dial = 50

    for line in file.readlines():
        direction = line[0]
        rotations = int(line[1:])

        if direction == "R":
            dial = (dial + rotations) % 100
        elif direction == "L":
            dial = (dial - rotations) % 100

        if dial == 0:
            password += 1

    file.close()
    return password


def part_two() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    password = 0
    dial = 50

    for line in file.readlines():
        direction = line[0]
        rotations = int(line[1:])

        for _ in range(rotations):
            if direction == "R":
                dial = (dial + 1) % 100
            elif direction == "L":
                dial = (dial - 1) % 100

            if dial == 0:
                password += 1

    file.close()
    return password


if __name__ == "__main__":
    print(part_one())
    print(part_two())
