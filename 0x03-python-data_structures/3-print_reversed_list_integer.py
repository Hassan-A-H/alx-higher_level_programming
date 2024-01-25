#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""

    new_list = my_list[::-1]
    for i in new_list:
        print("{:d}".format(i))
