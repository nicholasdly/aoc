# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import re


PATH = "./2024/3/"


def part_one() -> int:
    file = open(PATH + "input.txt")

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    expressions: list[str] = re.findall(pattern, file.read())

    total = 0

    for expression in expressions:
        operands = expression[4:-1].split(",")
        total += int(operands[0]) * int(operands[1])

    file.close()
    return total


def part_two() -> int:
    file = open(PATH + "input.txt")

    pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
    expressions: list[str] = re.findall(pattern, file.read())

    total = 0
    do = True

    for expression in expressions:
        if expression == "do()":
            do = True
        elif expression == "don't()":
            do = False
        elif do:
            operands = expression[4:-1].split(",")
            total += int(operands[0]) * int(operands[1])

    file.close()
    return total


if __name__ == "__main__":
    print(part_one())
    print(part_two())
