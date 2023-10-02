def insertion_sort(collection):
    for i in range(1, len(collection)):
        for j in range(i - 1, -1, -1):
            if collection[j + 1] < collection[j]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
    return collection
