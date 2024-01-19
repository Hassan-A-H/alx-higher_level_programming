#!/usr/bin/python3
def print_reversed_alphabet():
    for c in range(122, 96, -1):
        if c % 2 != 0:
            c = c - 32
        print("{}".format(chr(c)), end="")


print_reversed_alphabet()
