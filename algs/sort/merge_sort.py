def merge_sort(collection):
    split_merge(0, len(collection), collection)
    return collection


def split_merge(begin, end, collection):
    if (end - begin) > 0:
        middle = (end + begin) // 2
        split_merge(begin, middle, collection)
        split_merge(middle + 1, end, collection)
        merge(begin, middle, end, collection)


def merge(begin, middle, end, collection):
    left = collection[begin : middle + 1]
    right = collection[middle + 1 : end + 1]
    i = j = 0
    k = begin

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            collection[k] = left[i]
            i += 1
        else:
            collection[k] = right[j]
            j += 1
        k += 1

    if j == len(right):
        collection[k : end + 1] = left[i:]
