# aoc

My solutions to the [Advent of Code](https://adventofcode.com/) challenges. Input files are not included in this repository, but can be found on the official Advent of Code website.

```bash
# Download and install uv:
brew install uv

# Create a new script:
uv init ./[YEAR]/[DAY]/solution.py --script

# Format and lint code:
uvx ruff format

# Run a script:
uv run ./[YEAR]/[DAY]/solution.py
```

## Template

```python
import os

BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))


def part_one() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    # ...

    file.close()
    return 0


def part_two() -> int:
    file = open(os.path.join(BASE_DIRECTORY, "input.txt"))

    # ...

    file.close()
    return 0


if __name__ == "__main__":
    print(part_one())
    print(part_two())
```

## License

This project is open source and available under the [MIT License](LICENSE).
