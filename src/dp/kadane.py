# Find a contiguous subarray with the largest sum

# Kadane's algorithm calculates the maximum subarray ending at each position from the maximum subarray ending at the
# previous position

import math


def maximum_subarray_sum(numbers: list[int]) -> int:
    if not len(numbers):
        raise ValueError("input list cannot be empty")

    best_sum = -math.inf
    current_sum = 0

    for number in numbers:
        current_sum = max(number, current_sum + number)
        best_sum = max(best_sum, current_sum)
    return best_sum


print(maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maximum_subarray_sum([-2, -1, -3, -4, -1, -2, -1, -5, -4]))
print(maximum_subarray_sum([-2]))
print(maximum_subarray_sum([2]))
print(maximum_subarray_sum([]))
