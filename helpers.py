from os import path
from time import time
from typing import Callable


def log(func: Callable):
    """
    A decorator function for logging the result and execution time of a function.
    """

    def wrapper():
        start = time()
        result = func()
        end = time()

        print(f"{func.__name__} = {result} ({(end - start) * 1000:0.0f} ms)")

        return result

    return wrapper


def read_input(pathname: str, filename: str = "input.txt") -> str:
    """
    Reads and returns the contents of the `input.txt` file.
    """
    directory = path.abspath(path.dirname(pathname))
    with open(path.join(directory, filename)) as file:
        return file.read().strip()
