from enum import Enum


class Mode(Enum):
    UP = 1
    DOWN = 2
    HOURGLASS = 3
    RHOMB = 4


def print_triangle(height: int, mode: Mode, char: str = "*") -> None:

    match mode:
        case Mode.UP:
            print_up_triangle(height, char)
        case Mode.DOWN:
            print_down_triangle(height, char)
        case Mode.HOURGLASS:
            hide = (height % 2) != 0
            height = height // 2 if height % 2 == 0 else height // 2 + 1
            print_down_triangle(height, char)
            print_up_triangle(height, char, hide)
        case Mode.RHOMB:
            hide = (height % 2) != 0
            height = height // 2 if height % 2 == 0 else height // 2 + 1
            print_up_triangle(height, char)
            print_down_triangle(height, char, hide)


def print_down_triangle(height: int, char: str, hide_top: bool = False):
    row_count = height - 1 if hide_top else height
    for i in range(row_count, 0, -1):
        print(f"{(char + ' ') * ((2 * i) - 1):^{height * 4}}")


def print_up_triangle(height: int, char: str, hide_bottom: bool = False):
    start_row = 2 if hide_bottom else 1
    for i in range(start_row, height + 1):
        print(f"{(char + ' ') * ((2 * i) - 1):^{height * 4}}")


# print_triangle(8, Mode.UP)
# print_triangle(8, Mode.DOWN)
print("{:=^30}".format(" HOURGLASS 8 "))
print_triangle(8, Mode.HOURGLASS)
print("{:=^30}".format(" HOURGLASS 7 "))
print_triangle(7, Mode.HOURGLASS, ":")
print("{:=^30}".format(" RHOMB 8 "))
print_triangle(8, Mode.RHOMB, "o")
print("{:=^30}".format(" RHOMB 7 "))
print_triangle(7, Mode.RHOMB, "?")
