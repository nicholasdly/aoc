
class CPU:
    """
    Represents a simple CPU.
    """

    SIGNALS = { 20, 60, 100, 140, 180, 220 }  # Significant cycles

    def __init__(self):
        """
        Initializes a CPU.
        """
        self.register = 1  # The current register value
        self.clock = 1  # The current cycle
        self.history = {}  # A history of register values by cycle

    def noop(self):
        """
        Executes the 'noop' command, which takes 1
        cycle to run and does nothing other than that.
        """
        self.history[self.clock] = self.register
        self.clock += 1

    def addx(self, value: int):
        """
        Executes the 'addx' command, which takes 2 cycles to run
        and adds a specified value to the current register value.
        """
        self.history[self.clock] = self.register
        self.clock += 1
        self.history[self.clock] = self.register
        self.clock += 1
        self.register += value

    def command(self, command: list):
        """
        Executes a specified command.
        """
        match command[0]:
            case "noop":
                self.noop()
            case "addx":
                self.addx( int(command[1]) )
    
class CRT:
    """
    Represents the elves' cathode-ray tube screen.
    """

    ROWS, COLS = 6, 40  # Dimensions of the screen

    def __init__(self, instructions: list[list]):
        """
        Initializes a cathode-ray tube screen,
        lighting each pixel according to CPU timings.
        """
        self.screen = [ [ '.' for _ in range(self.COLS) ] for _ in range(self.ROWS) ]
        
        # Processes CPU instructions
        self.cpu = CPU()
        for command in instructions:
            self.cpu.command(command)

        # Draws screen according to sprite timing rules.
        for r in range(self.ROWS):
            for c in range(self.COLS):
                cycle = r * 40 + c + 1
                spriteLocation = {
                    self.cpu.history.get(cycle) - 1,
                    self.cpu.history.get(cycle),
                    self.cpu.history.get(cycle) + 1
                }
                if c in spriteLocation:
                    self.screen[r][c] = "#"

    def display(self):
        """
        Prints the cathode-ray tube screen.
        """
        for row in self.screen:
            print( " ".join(row) )

def partOne(instructions: list[list]):
    """
    Prints the sum of six significant signal strengths.
    """
    cpu = CPU()
    for command in instructions:
        cpu.command(command)
    print( sum([ cpu.history[r] * r for r in cpu.SIGNALS ]) )

def partTwo(instructions: list[list]):
    """
    Prints a cathode-ray tube screen according to its CPU instructions.
    """
    crt = CRT(instructions)
    crt.display()

def main():
    with open("input.txt", "r") as file:
        instructions = [ line.split() for line in file.readlines() ]
        partOne(instructions)
        partTwo(instructions)

if __name__ == "__main__":
    main()
