import queue
from dataclasses import dataclass
from typing import NamedTuple

type Graph = dict[str, list[Edge]]


@dataclass(frozen=True, slots=True)
class Edge:
    distance: int
    dest_node: str


@dataclass(frozen=True, slots=True)
class ShortestPath:
    path: str
    total_distance: int


class State(NamedTuple):
    distance: int
    node: str
    path: str


def dijkstra_shortest_path(graph: Graph, start: str, end: str) -> ShortestPath:
    visited: set[str] = set()
    next_nodes: queue.PriorityQueue[State] = queue.PriorityQueue()

    if start not in graph or end not in graph:
        raise ValueError("start/end nodes do not exist in graph")

    next_nodes.put(State(0, start, start))

    while next_nodes.qsize():
        current_distance, current_node, current_path = next_nodes.get()

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return ShortestPath(current_path, current_distance)

        for edge in graph[current_node]:
            if edge.dest_node in visited:
                continue

            next_nodes.put(
                State(
                    current_distance + edge.distance,
                    edge.dest_node,
                    f"{current_path} -> {edge.dest_node}",
                )
            )

    raise ValueError("graph cannot be empty")


g: Graph = {
    "a": [Edge(3, "b"), Edge(8, "c")],
    "b": [Edge(3, "a"), Edge(5, "d")],
    "c": [Edge(8, "a"), Edge(2, "d"), Edge(4, "e")],
    "d": [Edge(5, "b"), Edge(2, "c"), Edge(6, "e")],
    "e": [Edge(4, "c"), Edge(6, "d")],
}

print(dijkstra_shortest_path(g, "a", "e"))
print(dijkstra_shortest_path(g, "d", "a"))
print(dijkstra_shortest_path(g, "z", "x"))
