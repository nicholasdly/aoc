# aoc

My solutions to the [Advent of Code](https://adventofcode.com/) challenges.

## Getting Started

1. Download and install uv:

```bash
brew install uv
```

## Usage

To run a specific solution, run the associated script:

```bash
uv run ./[YEAR]/[DAY]/solution.py
```

> [!note]
> The puzzle text and input files are not included, and are actually added to the `.gitignore`, by request of Eric Wastl, the creator of Advent of Code. You can easily retrieve them for yourself from the Advent of Code website.
> > "If you're posting a code repository somewhere, please don't include parts of Advent of Code like the puzzle text or your inputs."

To run ruff, the linter and formatter, use the following command:

```bash
uvx ruff format
```

To create a new script, run the following command:

```bash
uv init ./[YEAR]/[DAY]/solution.py --script
```

## License

This project is open source and available under the [MIT License](LICENSE).
