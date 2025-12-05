# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path
from sys import path

path.insert(0, str(Path(__file__).parent.parent.parent))

from helpers import log, read_input


def parse_data(data: str) -> tuple[list[tuple[int, int]], list[int]]:
    sections = data.split("\n\n")

    ranges = [r.split("-") for r in sections[0].split()]
    ranges = [(int(r[0]), int(r[1])) for r in ranges]

    ids = [int(id) for id in sections[1].split()]

    return (ranges, ids)


@log
def part_one() -> int:
    data = read_input(__file__)
    ranges, ids = parse_data(data)

    fresh = 0

    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                fresh += 1
                break

    return fresh


@log
def part_two() -> int:
    data = read_input(__file__)
    ranges, _ = parse_data(data)

    ranges.sort()

    merged: list[tuple[int, int]] = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_merged_start, last_merged_end = merged[-1]

        if current_start <= last_merged_end:
            merged[-1] = (last_merged_start, max(current_end, last_merged_end))
        else:
            merged.append((current_start, current_end))

    return sum([end - start + 1 for start, end in merged])


if __name__ == "__main__":
    part_one()
    part_two()
