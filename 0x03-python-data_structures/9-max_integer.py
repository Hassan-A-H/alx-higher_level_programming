#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer of a list."""

    if len(my_list) == 0:
        return (None)
    max = my_list[0]
    for num in my_list:
        if num > max:
            max = num
    return (max)
