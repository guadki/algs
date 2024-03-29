import queue
from typing import Tuple


def dijkstra_shortest_path(graph: dict, start: str, end: str) -> Tuple[str, int]:
    visited = set()
    next_nodes = queue.PriorityQueue()

    if start not in graph or end not in graph:
        raise ValueError("start/end nodes do not exist in graph")

    next_nodes.put((0, (start, start)))

    while next_nodes.qsize():
        current_distance, (current_node, current_path) = next_nodes.get()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return current_path, current_distance

        for distance, node in graph[current_node]:
            if node in visited:
                continue

            next_nodes.put(
                (current_distance + distance, (node, " -> ".join([current_path, node])))
            )

    raise ValueError("graph cannot be empty")


g = {
    "a": [[3, "b"], [8, "c"]],
    "b": [[3, "a"], [5, "d"]],
    "c": [[8, "a"], [2, "d"], [4, "e"]],
    "d": [[5, "b"], [2, "c"], [6, "e"]],
    "e": [[4, "c"], [6, "d"]],
}

print(dijkstra_shortest_path(g, "a", "e"))
print(dijkstra_shortest_path(g, "d", "a"))
print(dijkstra_shortest_path(g, "z", "x"))
