
class File:

    def __init__(self, root, name, size):
        self.name = name
        self.size = size
        self.root = root
        self.children = []

    def __repr__(self):
        return f"(name={self.name}, size={self.size})"

    def __str__(self):
        output = f"{self.name}\n"
        for file in self.children:
            output += f"(file={file.name}, size={file.size})\n"
        return output

    def add(self, root, name, size):
        self.children.append(File(root, name, size))

def totalSize(file: File):
    size = file.size
    for child in file.children:
        size += totalSize(child)
    return size

def partOne(node: File, directorySizes: list[int]):
    if len(node.children) == 0:
        return
    directorySizes.append(totalSize(node))
    for child in node.children:
        partOne(child, directorySizes)

def partTwo(num):
    return 70000000 - 41735494 + num

def main():
    with open("input.txt", "r") as file:

        # List of terminal command arguments
        terminal = [line.split() for line in file.readlines()[1:]]
        
        # Construct a tree representation of the file system
        node = File(None, '/', 0)
        for line in terminal:
            if line[0] != '$':  # If not a command, add the file to the current directory
                size = int(line[0]) if line[0] != 'dir' else 0
                node.add(node, line[1], size)
            elif line[1] == 'cd':  # Otherwise change directory accordingly
                if line[2] == '..':
                    node = node.root
                else:
                    for file in node.children:
                        if file.name == line[2]:
                            node = file
                            break
        
        # Return to the root directory
        while node.root:
            node = node.root

        directorySizes = []
        partOne(node, directorySizes)
        print(totalSize(node))
        
        # part one
        total = 0
        for size in directorySizes:
            if size <= 100000:
                total += size
        print(total)

        # part two
        possibleDeletions = [ size for size in directorySizes if partTwo(size) >= 30000000 ]
        print(min(possibleDeletions))

if __name__ == "__main__":
    main()
