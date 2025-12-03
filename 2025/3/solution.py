# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import os

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))


def part_one() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    total = 0

    for bank in file.readlines():
        bank = bank.strip()

        joltage = 0

        for i, a in enumerate(bank[:-1]):
            for b in bank[i + 1 :]:
                joltage = max(joltage, int(a + b))

        total += joltage

    file.close()
    return total


def part_two() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    total = 0

    for line in file.readlines():
        bank = line.strip()

        stack: list[str] = []

        for i, battery in enumerate(bank):
            remaining = len(bank) - i

            while (
                len(stack) > 0
                and len(stack) + remaining > 12
                and int(stack[-1]) < int(battery)
            ):
                stack.pop()

            if len(stack) < 12:
                stack.append(battery)

        joltage = int("".join(stack))
        total += joltage

    file.close()
    return total


if __name__ == "__main__":
    print(part_one())
    print(part_two())
