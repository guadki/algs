import random


def quicksort(collection):
    quicksort_rec(collection, 0, len(collection) - 1)
    return collection


def quicksort_rec(collection, begin, end):
    if begin >= end:
        return

    # pivot = collection[((end - begin) // 2) + begin]
    pivot = collection[random.randint(begin, end)]
    # pivot = collection[end]

    # i - left index
    # j - right index
    i, j = begin, end

    while i <= j:
        # left side of pivot should have values smaller than pivot
        while collection[i] < pivot:
            i += 1
        # right side of pivot should have values bigger than pivot
        while collection[j] > pivot:
            j -= 1

        if i <= j:
            collection[i], collection[j] = collection[j], collection[i]
            i += 1
            j -= 1

    quicksort_rec(collection, begin, j)
    quicksort_rec(collection, i, end)
