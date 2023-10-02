import queue


def prims_mst(graph: dict, start: str) -> list[str]:
    """Prim's algorithm for finding Minimum Spanning Tree (MST) using priority queue"""
    adjacent_nodes = queue.PriorityQueue()
    visited = set()
    mst = []
    # for calculating cost of MST
    # cost = 0

    adjacent_nodes.put((0, start))

    while adjacent_nodes.qsize():
        dist, node = adjacent_nodes.get()

        if node in visited:
            continue

        mst += node
        visited.add(node)
        add_adjacent_nodes(node, adjacent_nodes, graph, visited)

        # for calculating cost of MST
        # cost += dist

    return mst


def add_adjacent_nodes(
    node: str, adjacent_nodes: queue.PriorityQueue, graph: dict, visited: set[str]
) -> None:
    """Add adjacent nodes of recently visited node"""
    for distance, adjacent in graph[node]:
        if adjacent not in visited:
            adjacent_nodes.put((distance, adjacent))


g = {
    "a": [[3, "b"], [8, "c"]],
    "b": [[3, "a"], [5, "d"]],
    "c": [[8, "a"], [2, "d"], [4, "e"]],
    "d": [[5, "b"], [2, "c"], [6, "e"]],
    "e": [[4, "c"], [6, "d"]],
}

print(prims_mst(g, "a"))
