def is_sorted(collection):
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            return False
    return True
