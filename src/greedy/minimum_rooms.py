# There are n student groups at the school. On each day in school, there are m time slots. A student group may or may
# not be free during a time slot. We are given n binary string where each binary string is of length m. A character
# at j-th position in i-th string is 0 if i-th group is free in j-th slot and 1 if i-th group is busy.
# Determine the minimum number of rooms needed to hold classes for all groups on a single study day.

# Input: ['0101010', '1010101']
# Output: 1

# Input: ['0101011', '0011001', '0110111']
# Output: 3


def minimum_rooms(slots: list[str]) -> int:
    slots = [int(slot, 2) for slot in slots]
    rooms = 1
    check = slots[0]
    for i in range(1, len(slots)):
        check &= slots[i]
        if check:
            rooms += 1
        else:
            return rooms
    return rooms


print(minimum_rooms(["0101010", "1010101"]))
print(minimum_rooms(["0101011", "0011001", "0110111"]))
