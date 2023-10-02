# Given numbers [1,3,5] return total number of ways to form number n.
from functools import cache


@cache
def number_of_arrangements(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1

    return (
        number_of_arrangements(n - 1)
        + number_of_arrangements(n - 3)
        + number_of_arrangements(n - 5)
    )


print(number_of_arrangements(34))
print(number_of_arrangements(1))
print(number_of_arrangements(6))
