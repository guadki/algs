def selection_sort(collection):
    length = len(collection)
    for i in range(0, length - 1):
        j_min = i
        for j in range(i + 1, length):
            if collection[j] < collection[j_min]:
                j_min = j

        if j_min != i:
            collection[i], collection[j_min] = collection[j_min], collection[i]
    return collection
