
def partOne(lines: list):
    totalAssignmentPairs = 0
    for line in lines:
        ranges = [
            line.strip().split(",")[0].split("-"),
            line.strip().split(",")[1].split("-")
        ]
        
        pair = [
            set(value for value in range(int(ranges[0][0]), int(ranges[0][1]) + 1)),
            set(value for value in range(int(ranges[1][0]), int(ranges[1][1]) + 1))
        ]

        if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
            totalAssignmentPairs += 1

    return totalAssignmentPairs
        

def partTwo(lines: list):
    totalAssignmentPairs = 0
    for line in lines:
        ranges = [
            line.strip().split(",")[0].split("-"),
            line.strip().split(",")[1].split("-")
        ]
        
        pair = [
            set(value for value in range(int(ranges[0][0]), int(ranges[0][1]) + 1)),
            set(value for value in range(int(ranges[1][0]), int(ranges[1][1]) + 1))
        ]

        if len(pair[0].intersection(pair[1])) > 0:
            totalAssignmentPairs += 1

    return totalAssignmentPairs

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        print(partOne(lines))
        print(partTwo(lines))

if __name__ == "__main__":
    main()
