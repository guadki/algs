def heap_sort(collection):
    length = len(collection)
    # Initial collection is virtually split. Heap on the left, unsorted items on right.
    # Take leftmost item from unsorted part and treat it like its appended to the end of the heap.
    # Then swim it up until its parent is larger than this item.
    for i in range(0, length):
        swim_up(i, collection)

    # Take the top of the heap (largest value), move last item to the top of heap, sink it down until both children
    # are smaller than this item
    for j in range(length - 1, -1, -1):
        collection[0], collection[j] = collection[j], collection[0]
        sink_down(0, collection, j)
    return collection


# parent floor(i - 1)/2
def swim_up(index, heap):
    parent_index = (index - 1) // 2
    if index > 0 and heap[index] > heap[parent_index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        swim_up(parent_index, heap)


# left 2i + 1
# right 2i + 2
def sink_down(index, heap, heap_size):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if heap_size > left and heap[smallest] < heap[left]:
        smallest = left
    if heap_size > right and heap[smallest] < heap[right]:
        smallest = right
    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        sink_down(smallest, heap, heap_size)
