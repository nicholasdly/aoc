
#     [G]         [P]         [M]    
#     [V]     [M] [W] [S]     [Q]    
#     [N]     [N] [G] [H]     [T] [F]
#     [J]     [W] [V] [Q] [W] [F] [P]
# [C] [H]     [T] [T] [G] [B] [Z] [B]
# [S] [W] [S] [L] [F] [B] [P] [C] [H]
# [G] [M] [Q] [S] [Z] [T] [J] [D] [S]
# [B] [T] [M] [B] [J] [C] [T] [G] [N]
#  1   2   3   4   5   6   7   8   9 

class SupplyStacks:
    """
    Represents the elves' supply crate stacks.
    """

    def __init__(self, stacks: list[list]):
        """
        Initializes the supply crate stacks.
        """
        self.stacks = stacks

    def tops(self) -> str:
        """
        Returns a string of all the top crates.
        """
        return "".join([ stack[-1] for stack in self.stacks ])

    def moveOne(self, count: int, start: int, destination: int):
        """
        Moves a number of crates from a start stack
        to a destination stack one at a time.
        """
        for _ in range(count):
            crate = self.stacks[start - 1].pop()
            self.stacks[destination - 1].append(crate)

    def moveMultiple(self, count: int, start: int, destination: int):
        """
        Moves a number of crates from a start stack
        to a destination stack multiple at a time.
        """
        holder = []
        for _ in range(count):
            holder.append(self.stacks[start - 1].pop())
        self.stacks[destination - 1].extend(holder[::-1])

def partOne(lines: list, stacks: SupplyStacks) -> str:
    for line in lines:
        count = int(line.split()[1])
        start = int(line.split()[3])
        destination = int(line.split()[5])
        stacks.moveOne(count, start, destination)
    return stacks.tops()

def partTwo(lines: list, stacks: list[list]) -> str:
    for line in lines:
        count = int(line.split()[1])    
        start = int(line.split()[3])
        destination = int(line.split()[5])
        stacks.moveMultiple(count, start, destination)
    return stacks.tops()

def main():
    stacks = [
        ['B', 'G', 'S', 'C'],
        ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
        ['M', 'Q', 'S'],
        ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
        ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
        ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
        ['T', 'J', 'P', 'B', 'W'],
        ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
        ['N', 'S', 'H', 'B', 'P', 'F']
    ]

    supply = SupplyStacks(stacks)
    with open("input.txt", "r") as file:
        lines = file.readlines()
        # print( partOne(lines, supply) )
        print( partTwo(lines, supply) )

if __name__ == "__main__":
    main()
