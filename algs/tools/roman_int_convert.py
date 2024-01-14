_conversion_list = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]


def int_to_roman(number: int) -> str:
    result = ""
    for roman, arabic in _conversion_list:
        (factor, number) = divmod(number, arabic)
        result += roman * factor
    return result


def roman_to_int(roman_numeral: str) -> int:
    result = 0
    index = 0

    for roman, arabic in _conversion_list:
        while roman_numeral[index : index + len(roman)] == roman:
            result += arabic
            index += len(roman)
    return result


print(int_to_roman(8))
print(int_to_roman(9))
print(int_to_roman(4))

print(roman_to_int("VIII"))
print(roman_to_int("IX"))
print(roman_to_int("IV"))