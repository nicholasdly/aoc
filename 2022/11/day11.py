
class Monkey:
    """
    Represents a monkey.
    """

    def __init__(self):
        """
        Initializes a monkey with no data.
        """
        self.items = []
        self.operation = None
        self.divisor = None
        self.throwTrue = None
        self.throwFalse = None
        self.inspects = 0

def makeMonkeys(lines: list[list[str]]) -> list[Monkey]:
    """
    Defines and returns the list of monkeys.
    """
    monkeys = []
    monkey = None

    for line in lines:
        if len(line) == 0:
            monkeys.append(monkey)
            continue

        match line[0].strip(':'):
            case 'Monkey':
                monkey = Monkey()
            case 'Starting':
                monkey.items = [ int(item.strip(',')) for item in line[2:] ]
            case 'Operation':
                monkey.operation = eval(f"lambda old : old {line[-2]} {line[-1]}")
            case 'Test':
                monkey.divisor = int(line[-1])
            case 'If':
                if line[1].strip(':') == 'true':
                    monkey.throwTrue = int(line[-1])
                elif line[1].strip(':') == 'false':
                    monkey.throwFalse = int(line[-1])

    monkeys.append(monkey)
    return monkeys

def partOne(monkeys: list[Monkey]):
    """
    Prints the level of monkey business after 20 rounds.
    """
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                worry = monkey.operation(item) // 3
                if worry % monkey.divisor == 0:
                    monkeys[monkey.throwTrue].items.append(worry)
                else:
                    monkeys[monkey.throwFalse].items.append(worry)
                monkey.inspects += 1
    
    totalInspects = sorted([ monkey.inspects for monkey in monkeys ])
    print( totalInspects[-1] * totalInspects[-2] )

def partTwo(monkeys: list[Monkey]):
    """
    Prints the level of monkey business after 10,000 rounds.
    """
    
    # NOTE: I very much was stumped on this; did a bit of research and
    # discovered the Chinese remainder theorem. Check it out here:
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    crt = 1
    for monkey in monkeys:
        crt *= monkey.divisor

    for _ in range(10_000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                worry = monkey.operation(item) % crt
                if worry % monkey.divisor == 0:
                    monkeys[monkey.throwTrue].items.append(worry)
                else:
                    monkeys[monkey.throwFalse].items.append(worry)
                monkey.inspects += 1
    
    totalInspects = sorted([ monkey.inspects for monkey in monkeys ])
    print( totalInspects[-1] * totalInspects[-2] )

def main():
    with open('input.txt', 'r') as file:
        lines = [ line.split() for line in file.readlines() ]
        partOne( makeMonkeys(lines) )
        partTwo( makeMonkeys(lines) )

if __name__ == "__main__":
    main()
