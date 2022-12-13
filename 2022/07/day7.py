
class File:
    """
    Represents a file in the file system.
    """

    def __init__(self, root: 'File', name: str, size: int):
        """
        Initializes a file.
        """
        self.children = []
        self.root = root
        self.name = name
        self.size = size

class FileSystem:
    """
    Represents the elf file system.
    """

    MAX_STORAGE = 70000000  # Maximum allowed storage
    NEEDED_STORAGE = 30000000  # Necessary free storage for the update

    def __init__(self, terminal: list[list[str]]):
        """
        Initializes the file system.
        """
        # Construct a tree representation of the file system
        self.root = File(None, '/', 0)
        for line in terminal:
            if line[0] != '$':  # If not a command, add the file to the current directory
                size = int(line[0]) if line[0] != 'dir' else 0
                self.root.children.append(File(self.root, line[1], size))
            elif line[1] == 'cd':  # Otherwise change directory accordingly
                if line[2] == '..':
                    self.root = self.root.root
                else:
                    for file in self.root.children:
                        if file.name == line[2]:
                            self.root = file
                            break
        
        # Return to the root directory
        while self.root.root:
            self.root = self.root.root

    def getSize(self, file: File) -> int:
        """
        Returns the size of a directory.
        """
        size = file.size
        for child in file.children:
            size += self.getSize(child)
        return size

    def getUsedStorage(self) -> int:
        """
        Returns the amount of storage that is used by the file system.
        """
        return self.getSize(self.root)

    def getDirectorySizes(self, file: File) -> list[int]:
        """
        Returns a list of every directory's size in the file system.
        """
        directorySizes = []
        self._helperDirectorySizes(file, directorySizes)
        return directorySizes

    def _helperDirectorySizes(self, file: File, directorySizes: list[int]):
        """
        A recursive helper function for getDirectorySizes.
        """
        if len(file.children) == 0:
            return
        directorySizes.append(self.getSize(file))
        for child in file.children:
            self._helperDirectorySizes(child, directorySizes)

def partOne(system: FileSystem):
    """
    Prints the sum of all directory sizes less than
    100,000 in the file system.
    """
    total = 0
    for size in system.getDirectorySizes(system.root):
        if size <= 100000:
            total += size
    print(total)

def partTwo(system: FileSystem):
    """
    Prints the size of the smallest directory in which after being removed
    would leave enough storage for the update.
    """
    possibleDeletions = []
    # Saves all directory sizes which would leave enough room for the update
    for size in system.getDirectorySizes(system.root):
        leftover_storage = system.MAX_STORAGE - system.getUsedStorage() + size
        if leftover_storage >= system.NEEDED_STORAGE:
            possibleDeletions.append(size)
    print( min(possibleDeletions) )  # Prints the minimum of the saved sizes

def main():
    with open("input.txt", "r") as file:

        # List of terminal command arguments
        terminal = [line.split() for line in file.readlines()[1:]]

        system = FileSystem(terminal)
        partOne(system)
        partTwo(system)

if __name__ == "__main__":
    main()
