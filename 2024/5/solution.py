# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

PATH = "./2024/5/"


def topological_sort(graph: dict[int, set[int]]) -> list[int]:
    visited = set()
    topological_order = []

    def dfs(graph: dict[int, set[int]], node: int) -> None:
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor)

        topological_order.append(node)

    for node in graph:
        if node not in visited:
            dfs(graph, node)

    return topological_order


def part_one() -> int:
    with open(PATH + "input.txt") as file:
        sections = file.read().split("\n\n")

    rules = set(tuple(map(int, line.split("|"))) for line in sections[0].splitlines())
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]

    result = 0

    for update in updates:
        is_valid = True
        indices = {page: index for index, page in enumerate(update)}

        for x, y in rules:
            if x in indices and y in indices and indices[x] > indices[y]:
                is_valid = False
                break

        if is_valid:
            result += update[len(update) // 2]

    return result


def part_two() -> int:
    with open(PATH + "input.txt") as file:
        sections = file.read().split("\n\n")

    rules = set(tuple(map(int, line.split("|"))) for line in sections[0].splitlines())
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]

    result = 0

    for update in updates:
        is_valid = True
        indices = {page: index for index, page in enumerate(update)}

        for x, y in rules:
            if x in indices and y in indices and indices[x] > indices[y]:
                is_valid = False
                break

        if is_valid:
            continue

        update = set(update)
        graph: dict[int, set[int]] = {}

        for x, y in rules:
            if x in update and y in update:
                graph[x] = graph.get(x, set())
                graph[y] = graph.get(y, set())
                graph[x].add(y)

        update = topological_sort(graph)
        result += update[len(update) // 2]

    return result


if __name__ == "__main__":
    print(part_one())
    print(part_two())
