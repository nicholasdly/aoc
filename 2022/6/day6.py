
def partOne(line: str) -> str:
    """
    Finds the character in a string where the previous four characters were all unique.
    """
    marker = list(line[:4])
    for pos, char in enumerate(line[4:], 4):
        if len(set(marker)) < 4:
            marker.pop(0)
            marker.append(char)
        else:
            return str(pos)

def partTwo(line: str) -> str:
    """
    Finds the character in a string where the previous fourteen characters were all unique.
    """
    marker = list(line[:14])
    for pos, char in enumerate(line[14:], 14):
        if len(set(marker)) < 14:
            marker.pop(0)
            marker.append(char)
        else:
            return str(pos)

def main():
    with open("input.txt", "r") as file:
        line = file.readline()
        print( partOne(line) )
        print( partTwo(line) )

if __name__ == "__main__":
    main()
