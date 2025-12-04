# /// script
# requires-python = ">=3.14"
# dependencies = []
# ///

from pathlib import Path
from sys import path

path.insert(0, str(Path(__file__).parent.parent.parent))

from helpers import log, read_input


@log
def part_one() -> int:
    grid = [[c for c in line] for line in read_input(__file__).split("\n")]

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
    grid = [[c for c in line] for line in read_input(__file__).split("\n")]

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
