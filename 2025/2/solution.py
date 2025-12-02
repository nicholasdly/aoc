# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

import os

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))


def part_one() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    ranges: list[tuple[int, int]] = []

    for r in file.read().split(","):
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    invalid: set[int] = set()

    for start, end in ranges:
        for n in range(start, end + 1):
            id = str(n)

            if len(id) % 2 != 0:
                continue

            if id[: len(id) // 2] == id[len(id) // 2 :]:
                invalid.add(n)

    file.close()
    return sum(invalid)


def part_two() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    ranges: list[tuple[int, int]] = []

    for r in file.read().split(","):
        start, end = map(int, r.split("-"))
        ranges.append((start, end))

    invalid: set[int] = set()

    for start, end in ranges:
        for n in range(start, end + 1):
            id = str(n)

            for length in range(1, len(id) // 2 + 1):
                if len(id) % length != 0:
                    continue

                if id[:length] * (len(id) // length) == id:
                    invalid.add(n)

    file.close()
    return sum(invalid)


if __name__ == "__main__":
    print(part_one())
    print(part_two())
