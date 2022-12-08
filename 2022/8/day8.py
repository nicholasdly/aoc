from dataclasses import dataclass

@dataclass(kw_only=True, slots=True)
class Tree:
    """
    Represents a tree in a forest.
    """
    height: int
    visible: bool = False

def computeScenicScore(forest: list[list[Tree]], row: int, col: int) -> int:
    """
    Computes the scenic score of a tree at a specified location in the forest.
    """
    length = len(forest)  # NOTE: Assumes forest is a square matrix
    distances = {
        'right' : 0,
        'down' : 0,
        'left' : 0,
        'up' : 0
    }

    # Counts all trees visible by looking right
    vision = col + 1
    while vision < length:
        distances['right'] += 1
        if forest[row][vision].height >= forest[row][col].height:
            break
        vision += 1

    # Counts all trees visible by looking down
    vision = row + 1
    while vision < length:
        distances['down'] += 1
        if forest[vision][col].height >= forest[row][col].height:
            break
        vision += 1

    # Counts all trees visible by looking left
    vision = col - 1
    while vision >= 0:
        distances['left'] += 1
        if forest[row][vision].height >= forest[row][col].height:
            break
        vision -= 1

    # Counts all trees visible by looking up
    vision = row - 1
    while vision >= 0:
        distances['up'] += 1
        if forest[vision][col].height >= forest[row][col].height:
            break
        vision -= 1

    return distances['right'] * distances['down'] * distances['left'] * distances['up']

def partOne(forest: list[list[Tree]]):
    """
    Prints the number of visible trees from outside the forest.
    """
    length = len(forest)  # NOTE: Assumes forest is a square matrix

    # Mark all trees visible by looking down or right
    for a in range(length):
        tallestRight = -1
        tallestDown = -1
        for b in range(length):
            if forest[a][b].height > tallestRight:  # Is visible looking right?
                forest[a][b].visible = True
                tallestRight = forest[a][b].height
            if forest[b][a].height > tallestDown:  # Is visible looking down?
                forest[b][a].visible = True
                tallestDown = forest[b][a].height

    # Mark all trees visible by looking up or left
    for a in range(length - 1, 0, -1):
        tallestLeft = -1
        tallestUp = -1
        for b in range(length - 1, 0, -1):
            if forest[a][b].height > tallestLeft:  # Is visible looking left?
                forest[a][b].visible = True
                tallestLeft = forest[a][b].height
            if forest[b][a].height > tallestUp:  # Is visible looking up?
                forest[b][a].visible = True
                tallestUp = forest[b][a].height

    # Counts all visible trees
    counter = 0
    for row in forest:
        for tree in row:
            if tree.visible:
                counter += 1
    print( counter )

def partTwo(forest: list[list[Tree]]):
    """
    Prints the highest 'scenic score' possible for any tree in the forest.
    """
    length = len(forest)  # NOTE: Assumes forest is a square matrix
    highestScenicScore = 0
    for row in range(length):
        for col in range(length):
            score = computeScenicScore(forest, row, col)
            if score > highestScenicScore:
                highestScenicScore = score
    print( highestScenicScore )

def main():
    with open("input.txt", "r") as file:
        forest = [ [ Tree(height=int(height)) for height in row.strip() ] for row in file.readlines() ]
        partOne(forest)
        partTwo(forest)

if __name__ == "__main__":
    main()
