
LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

PRIORITIES = {
    itemType : priority for priority, itemType in enumerate(LETTERS, 1)
}

def partOne():
    sumOfPriorities = 0
    with open('input.txt', 'r') as file:
        for record in file.readlines():
            itemTypes = [
                set(record.strip()[:len(record) // 2]),
                set(record.strip()[len(record) // 2:])
            ]
            mutualItemType = list(itemTypes[0].intersection(itemTypes[1]))[0]
            sumOfPriorities += PRIORITIES[mutualItemType]
    print(sumOfPriorities)

def partTwo():
    sumOfPriorities = 0
    with open('input.txt', 'r') as file:
        records = file.readlines()
        for i in range(0, len(records), 3):
            itemTypes = [
                set(records[i].strip()),
                set(records[i+1].strip()),
                set(records[i+2].strip())
            ]
            mutualItemType = list(itemTypes[0].intersection(itemTypes[1], itemTypes[2]))[0]
            sumOfPriorities += PRIORITIES[mutualItemType]
    print(sumOfPriorities)



if __name__ == "__main__":
    partOne()
    partTwo()
