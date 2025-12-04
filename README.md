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
from pathlib import Path
from sys import path

path.insert(0, str(Path(__file__).parent.parent.parent))

from helpers import log, read_input


@log
def part_one() -> int:
    data = read_input(__file__)  # Reads `input.txt` file
    return 0


@log
def part_two() -> int:
    data = read_input(__file__, "example.txt")  # Reads `example.txt` file
    return 0


if __name__ == "__main__":
    part_one()
    part_two()
```

```
part_one = 0 (1 ms)
part_two = 0 (1 ms)
```

## License

This project is open source and available under the [MIT License](LICENSE).
