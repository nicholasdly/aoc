# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///


PATH = "./2024/4/"


def search(
    matrix: list[list[str]],
    r: int,
    c: int,
    dr: int,
    dc: int,
    progress: str,
    word: str = "XMAS",
) -> int:
    """
    Searches a two-dimensional list of characters `matrix` for the string
    `word` as if it were a traditional word search puzzle.

    Requires the row index and column index of a letter in the word search to
    begin its search.

    :param matrix: A two-dimensional list of characters, or word search.
    :param r: The row index of the first letter.
    :param c: The column index of the first letter.
    :param dr: The row index delta, or the number of vertical steps made to look for the next letter.
    :param dc: The column index delta, or the number of horizontal steps made to look for the next letter.
    :param progress: A snapshot of the current word search progress.
    :returns `int`: Returns `1` if the complete word was found, otherwise returns `0`.
    """
    is_valid_row = 0 <= (r + dr) < len(matrix)
    if not is_valid_row:
        return 0

    is_valid_column = 0 <= (c + dc) < len(matrix[r])
    if not is_valid_column:
        return 0

    is_valid_letter = word.startswith(progress + matrix[r + dr][c + dc])
    if not is_valid_letter:
        return 0

    is_complete = progress + matrix[r + dr][c + dc] == word
    if is_complete:
        return 1

    return search(matrix, r + dr, c + dc, dr, dc, progress + matrix[r + dr][c + dc])


def part_one() -> int:
    with open(PATH + "input.txt") as file:
        lines = file.readlines()

    wordsearch = [[c for c in line.strip()] for line in lines]
    count = 0

    # Iterates over every character of the word search looking for the letter
    # 'X', which marks the potential start of the word "XMAS".
    for r, line in enumerate(wordsearch):
        for c, letter in enumerate(line):
            if letter != "X":
                continue

            offsets = [
                (-1, -1),  # Northwest
                (0, -1),  # North
                (1, -1),  # Northeast
                (-1, 0),  # West
                (1, 0),  # East
                (-1, 1),  # Southwest
                (0, 1),  # South
                (1, 1),  # Southeast
            ]

            for dr, dc in offsets:
                count += search(wordsearch, r, c, dr, dc, letter)

    return count


def part_two() -> int:
    with open(PATH + "input.txt") as file:
        lines = file.readlines()

    count = 0

    # Iterates over every character of the word search looking for the letter
    # 'A', which marks the potential center of an X formed by "MAS" strings.
    for r, line in enumerate(lines):
        for c, letter in enumerate(line):
            is_valid_x = (
                0 <= (r - 1) < len(lines)
                and 0 <= (r + 1) < len(lines)
                and 0 <= (c - 1) < len(lines[r])
                and 0 <= (c + 1) < len(lines[r])
            )

            if letter != "A" or not is_valid_x:
                continue

            # The two segments of the X-shape concatenated into their own strings.
            a = lines[r - 1][c - 1] + letter + lines[r + 1][c + 1]
            b = lines[r - 1][c + 1] + letter + lines[r + 1][c - 1]

            if (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM"):
                count += 1

    return count


if __name__ == "__main__":
    print(part_one())
    print(part_two())
