# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from os import path
from time import time
from typing import Callable


def log(func: Callable):
    def wrapper():
        start = time()
        result = func()
        end = time()

        print(f"{func.__name__} = {result} ({(end - start) * 1000:0.0f} ms)")

        return result

    return wrapper


def read_input() -> list[list[str]]:
    directory = path.abspath(path.dirname(__file__))
    with open(path.join(directory, "input.txt")) as file:
        return [[c for c in line] for line in file.read().strip().split("\n")]


@log
def part_one() -> int:
    grid = read_input()

    rows = len(grid)
    cols = len(grid[0])

    accessible_rolls = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adjacent_rolls = 0

            if r > 0 and c > 0 and grid[r - 1][c - 1] == "@":
                adjacent_rolls += 1
            if r > 0 and grid[r - 1][c] == "@":
                adjacent_rolls += 1
            if r > 0 and c < cols - 1 and grid[r - 1][c + 1] == "@":
                adjacent_rolls += 1
            if c > 0 and grid[r][c - 1] == "@":
                adjacent_rolls += 1
            if c < cols - 1 and grid[r][c + 1] == "@":
                adjacent_rolls += 1
            if r < rows - 1 and c > 0 and grid[r + 1][c - 1] == "@":
                adjacent_rolls += 1
            if r < rows - 1 and grid[r + 1][c] == "@":
                adjacent_rolls += 1
            if r < rows - 1 and c < cols - 1 and grid[r + 1][c + 1] == "@":
                adjacent_rolls += 1

            if adjacent_rolls < 4:
                accessible_rolls += 1

    return accessible_rolls


@log
def part_two() -> int:
    grid = read_input()

    rows = len(grid)
    cols = len(grid[0])

    total_removed_rolls = 0

    while True:
        accessible_rolls = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue

                adjacent_rolls = 0

                if r > 0 and c > 0 and grid[r - 1][c - 1] == "@":
                    adjacent_rolls += 1
                if r > 0 and grid[r - 1][c] == "@":
                    adjacent_rolls += 1
                if r > 0 and c < cols - 1 and grid[r - 1][c + 1] == "@":
                    adjacent_rolls += 1
                if c > 0 and grid[r][c - 1] == "@":
                    adjacent_rolls += 1
                if c < cols - 1 and grid[r][c + 1] == "@":
                    adjacent_rolls += 1
                if r < rows - 1 and c > 0 and grid[r + 1][c - 1] == "@":
                    adjacent_rolls += 1
                if r < rows - 1 and grid[r + 1][c] == "@":
                    adjacent_rolls += 1
                if r < rows - 1 and c < cols - 1 and grid[r + 1][c + 1] == "@":
                    adjacent_rolls += 1

                if adjacent_rolls < 4:
                    accessible_rolls += 1
                    grid[r][c] = "."

        if accessible_rolls == 0:
            break

        total_removed_rolls += accessible_rolls

    return total_removed_rolls


if __name__ == "__main__":
    part_one()
    part_two()
