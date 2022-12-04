
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
PRIORITIES = { itemType : priority for priority, itemType in enumerate(LETTERS, 1) }

def partOne(lines: list):
    sumOfPriorities = 0
    for line in lines:
        rucksack = [
            set(line.strip()[:len(line) // 2]),
            set(line.strip()[len(line) // 2:])
        ]
        mutualItemType = list(rucksack[0].intersection(rucksack[1]))[0]
        sumOfPriorities += PRIORITIES[mutualItemType]
    return sumOfPriorities

def partTwo(lines: list):
    sumOfPriorities = 0
    for i in range(0, len(lines), 3):
        rucksacks = [
            set(lines[i].strip()),
            set(lines[i+1].strip()),
            set(lines[i+2].strip())
        ]
        mutualItemType = list(rucksacks[0].intersection(rucksacks[1], rucksacks[2]))[0]
        sumOfPriorities += PRIORITIES[mutualItemType]
    return sumOfPriorities

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        print(partOne(lines))
        print(partTwo(lines))

if __name__ == "__main__":
    main()
