
# TODO: Rock-Paper-Scissors can be represented as binary:
# Rock = 100, Paper = 010, Scissors = 001

MOVE_POINTS = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

def computeScore(playerMove: str, opponentMove: str):
    if (playerMove == 'X' and opponentMove == 'C') \
            or (playerMove == 'Y' and opponentMove == 'A') \
            or (playerMove == 'Z' and opponentMove == 'B'):
        return MOVE_POINTS[playerMove] + 6  # Win
    elif (playerMove == 'X' and opponentMove == 'B') \
            or (playerMove == 'Y' and opponentMove == 'C') \
            or (playerMove == 'Z' and opponentMove == 'A'):
        return MOVE_POINTS[playerMove]  # Lose
    else:
        return MOVE_POINTS[playerMove] + 3  # Draw

def computeLosingScore(opponentMove: str):
    if opponentMove == 'A':
        return computeScore('Z', opponentMove)
    elif opponentMove == 'B':
        return computeScore('X', opponentMove)
    elif opponentMove == 'C':
        return computeScore('Y', opponentMove)
    raise Exception("Invalid opponent move")

def computeWinningScore(opponentMove: str):
    if opponentMove == 'A':
        return computeScore('Y', opponentMove)
    elif opponentMove == 'B':
        return computeScore('Z', opponentMove)
    elif opponentMove == 'C':
        return computeScore('X', opponentMove)
    raise Exception("Invalid opponent move")

def computeDrawingScore(opponentMove: str):
    if opponentMove == 'A':
        return computeScore('X', opponentMove)
    elif opponentMove == 'B':
        return computeScore('Y', opponentMove)
    elif opponentMove == 'C':
        return computeScore('Z', opponentMove)
    raise Exception("Invalid opponent move")

def partOne(lines: list):
    totalScore = 0
    for line in lines:
        playerMove, opponentMove = line[2], line[0]
        totalScore += computeScore(playerMove, opponentMove)    
    return totalScore

def partTwo(lines: list):
    totalScore = 0
    for line in lines:
        playerMove, opponentMove = line[2], line[0]
        if playerMove == 'X':
            totalScore += computeLosingScore(opponentMove) # Lose
        elif playerMove == 'Y':
            totalScore += computeDrawingScore(opponentMove)  # Draw
        elif playerMove == 'Z':
            totalScore += computeWinningScore(opponentMove)  # Win
    return totalScore

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        print(partOne(lines))
        print(partTwo(lines))

if __name__ == "__main__":
    main()
