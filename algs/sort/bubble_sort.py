def bubble_sort(collection):
    length = len(collection)
    swapped = True
    # end if there were no swaps in a run
    while swapped is True:
        swapped = False
        for i in range(0, length - 1):
            if collection[i] > collection[i + 1]:
                # swap
                collection[i], collection[i + 1] = collection[i + 1], collection[i]
                swapped = True
    return collection
