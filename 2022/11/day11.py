
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
        self.test = None
        self.throwTrue = None
        self.throwFalse = None
        self.inspects = 0

def partOne(monkies: list[Monkey]):
    """
    Prints the level of monkey business after 20 rounds.
    """
    for _ in range(20):
        for monkey in monkies:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                worry = monkey.operation(item) // 3
                if monkey.test(worry):
                    monkies[monkey.throwTrue].items.append(worry)
                else:
                    monkies[monkey.throwFalse].items.append(worry)
                monkey.inspects += 1
    
    totalInspects = sorted([ monkey.inspects for monkey in monkies ])
    print( totalInspects[-1] * totalInspects[-2] )

def partTwo(monkies: list[Monkey]):
    """
    Prints the level of monkey business after 10,000 rounds.
    """
    for _ in range(10_000):
        for monkey in monkies:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                worry = monkey.operation(item)
                if monkey.test(worry):
                    monkies[monkey.throwTrue].items.append(worry)
                else:
                    monkies[monkey.throwFalse].items.append(worry)
                monkey.inspects += 1
    
    totalInspects = sorted([ monkey.inspects for monkey in monkies ])
    print( totalInspects[-1] * totalInspects[-2] )

def main():
    with open('input.txt', 'r') as file:
        lines = [ line.split() for line in file.readlines() ]

        monkies = []
        monkey = None

        for line in lines:
            if len(line) == 0:
                monkies.append(monkey)
                continue

            match line[0].strip(':'):
                case 'Monkey':
                    monkey = Monkey()
                case 'Starting':
                    monkey.items = [ int(item.strip(',')) for item in line[2:] ]
                case 'Operation':
                    monkey.operation = eval(f"lambda old : old {line[-2]} {line[-1]}")
                case 'Test':
                    monkey.test = eval(f"lambda item : item % {line[-1]} == 0")
                case 'If':
                    if line[1].strip(':') == 'true':
                        monkey.throwTrue = int(line[-1])
                    elif line[1].strip(':') == 'false':
                        monkey.throwFalse = int(line[-1])

        monkies.append(monkey)
        partOne(monkies)
        partTwo(monkies)

if __name__ == "__main__":
    main()
