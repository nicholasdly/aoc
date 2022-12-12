from dataclasses import dataclass

@dataclass(slots=True)
class Knot:
    """
    Represents a knot in a rope.
    """
    x: int = 0
    y: int = 0

class Rope:
    """
    Represents a rope made up of knots.
    """

    def __init__(self, length: int):
        """
        Initailizes a rope of specified length.
        """
        self.rope = [ Knot() for _ in range(length) ]
        self.visited = { (0, 0) }  # Hashset of points visited by 'tail' knot
    
    def move(self, direction: str, steps: int):
        """
        Moves the rope by the 'head' in a specified
        direction and a specified distance.
        """
        for _ in range(steps):

            # Start by moving head in specified direction
            match direction:
                case 'U':
                    self.rope[0].y += 1
                case 'D':
                    self.rope[0].y -= 1
                case 'L':
                    self.rope[0].x -= 1
                case 'R':
                    self.rope[0].x += 1

            # Then move the rest of the rope based off of prior movement
            for i, knot in enumerate(self.rope[1:], 1):
                dx = knot.x - self.rope[i - 1].x
                dy = knot.y - self.rope[i - 1].y

                if (dx**2 + dy**2) ** (1/2) >= 2:

                    # Check for x-axis movement (and diagonals)
                    if dx == 2:
                        if dy == 1:
                            knot.y -= 1
                        elif dy == -1:
                            knot.y += 1
                        knot.x -= 1
                    elif dx == -2:
                        if dy == 1:
                            knot.y -= 1
                        elif dy == -1:
                            knot.y += 1
                        knot.x += 1

                    # Check for y-axis movement (and diagonals)
                    if dy == 2:
                        if dx == 1:
                            knot.x -= 1
                        elif dx == -1:
                            knot.x += 1
                        knot.y -= 1
                    elif dy == -2:
                        knot.y += 1
                        if dx == 1:
                            knot.x -= 1
                        elif dx == -1:
                            knot.x += 1
                            
            # Saves the position of 'tail' knot
            self.visited.add( (knot.x, knot.y) )

def partOne(moves: list[tuple[str, int]]):
    """
    Prints the number of unique points the 'tail' of
    a rope of 2 knots travels after a set of moves.
    """
    rope = Rope(2)
    for direction, steps in moves:
        rope.move(direction, steps)
    print( len(rope.visited) )
        
def partTwo(moves: list[tuple[str, int]]):
    """
    Prints the number of unique points the 'tail' of
    a rope of 10 knots travels after a set of moves.
    """
    rope = Rope(10)
    for direction, steps in moves:
        rope.move(direction, steps)
    print( len(rope.visited) )

def main():
    with open("input.txt", "r") as file:
        moves = [ (line.split()[0], int(line.split()[1])) for line in file.readlines() ]
        partOne(moves)
        partTwo(moves)

if __name__ == "__main__":
    main()
