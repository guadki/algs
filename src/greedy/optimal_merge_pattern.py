import queue


def optimal_merge_pattern(files: list[int]) -> int:
    files_queue = queue.PriorityQueue(len(files))
    for file in files:
        files_queue.put(file)

    min_cost = 0

    while files_queue.qsize() > 1:
        size = files_queue.get()
        size += files_queue.get()
        min_cost += size
        files_queue.put(size)

    return min_cost


print(optimal_merge_pattern([4, 5, 2, 7, 3, 6]))
