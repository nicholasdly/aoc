# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

from queue import PriorityQueue

PATH = "./2024/1/"


def part_one() -> int:
    file = open(PATH + "input.txt")

    left_list = PriorityQueue()
    right_list = PriorityQueue()

    for line in file.readlines():
        numbers = line.split()
        left_list.put(int(numbers[0]))
        right_list.put(int(numbers[1]))

    total = 0
    for _ in range(left_list.qsize()):
        total += abs(left_list.get() - right_list.get())

    file.close()
    return total


def part_two() -> int:
    file = open(PATH + "input.txt")

    left_list: list[int] = []
    right_counts: dict[int, int] = {}

    for line in file.readlines():
        numbers = line.split()

        left = int(numbers[0])
        right = int(numbers[1])

        left_list.append(left)
        right_counts[right] = right_counts.get(right, 0) + 1

    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_counts.get(number, 0)

    file.close()
    return similarity_score


if __name__ == "__main__":
    print("Part One Solution ::", part_one())
    print("Part Two Solution ::", part_two())
