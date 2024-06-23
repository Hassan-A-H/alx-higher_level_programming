#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer"""

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True