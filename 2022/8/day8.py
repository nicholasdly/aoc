from dataclasses import dataclass

@dataclass(kw_only=True, slots=True)
class Tree:
    """
    Represents a tree in a forest.
    """
    height: int
    visible: bool = False

def markOutsideVisbleTrees(forest: list[list[Tree]]):
    """
    Marks all trees in a forest visible only if they are visible from outside the forest.
    """
    length = len(forest)  # Assumes forest is a square matrix

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

def partOne(forest: list[list[int]]):
    """
    Prints the number of visible trees from outside the forest.
    """
    markOutsideVisbleTrees(forest)
    counter = 0
    for row in forest:
        for tree in row:
            if tree.visible:
                counter += 1
    print(counter)

def main():
    with open("input.txt", "r") as file:
        forest = [ [ Tree(height=int(height)) for height in row.strip() ] for row in file.readlines() ]
        partOne(forest)

if __name__ == "__main__":
    main()
