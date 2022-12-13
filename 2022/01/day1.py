
def partOne(lines: list):
    maxCalories = 0
    calories = 0
    for line in lines:
        if len(line.strip()) > 0:
            calories += int(line.strip())
        else:
            if calories > maxCalories:
                maxCalories = calories
            calories = 0
    return maxCalories

def partTwo(lines: list):
    allCalories = []
    calories = 0
    for line in lines:
        if len(line.strip()) > 0:
            calories += int(line.strip())
        else:
            allCalories.append(calories)
            calories = 0
    return sum(sorted(allCalories, reverse=True)[:3])

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        print(partOne(lines))
        print(partTwo(lines))

if __name__ == "__main__":
    main()
