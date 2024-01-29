#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""

    if type(roman_string) is not str or roman_string is None:
        return (0)

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    roman_list = [roman_dict[x] for x in roman_string]
    for i in range(len(roman_list)):
        result += roman_list[i]
        if roman_list[i - 1] < roman_list[i] and i != 0:
            result -= (2 * roman_list[i - 1])
    return (result)
