# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

PATH = "./2024/2/"


def is_report_safe(labels: list[str]) -> bool:
    increasing = True
    decreasing = True
    safe = True

    for index, value in enumerate(labels[1:], 1):
        previous = int(labels[index - 1])
        current = int(value)

        difference = current - previous

        if abs(difference) == 0 or abs(difference) > 3:
            safe = False

        if difference > 0:
            decreasing = False
        elif difference < 0:
            increasing = False

    return (increasing ^ decreasing) and safe


def part_one() -> int:
    file = open(PATH + "input.txt")

    count = 0

    for report in file.readlines():
        labels = report.split()

        if is_report_safe(labels):
            count += 1

    file.close()
    return count


def part_two() -> int:
    file = open(PATH + "input.txt")

    count = 0

    for report in file.readlines():
        labels = report.split()

        if is_report_safe(labels):
            count += 1
            continue

        for index, _ in enumerate(labels):
            if is_report_safe(labels[:index] + labels[index + 1 :]):
                count += 1
                break

    file.close()
    return count


if __name__ == "__main__":
    print(part_one())
    print(part_two())
