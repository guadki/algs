# the goal is to fill a container (the "knapsack") with fractional amounts of different materials chosen to maximize
# the value of the selected materials.
from collections import namedtuple
from fractions import Fraction

Material = namedtuple("Material", ["weight", "value"])


def continuous_knapsack_problem(materials: list[Material], knapsack_capacity: int):
    materials.sort(key=lambda m: m.value / m.weight, reverse=True)
    profit = 0

    for material in materials:
        if knapsack_capacity - material.weight > 0:
            knapsack_capacity -= material.weight
            profit += material.value
        elif knapsack_capacity - material.weight < 0:
            weight_fraction = Fraction(knapsack_capacity, material.weight)
            profit += material.value * weight_fraction
            break
        else:
            profit += material.value
            break

    return profit


print(
    continuous_knapsack_problem(
        [Material(10, 60), Material(20, 100), Material(30, 120)], 50
    )
)
