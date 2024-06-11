#!/usr/bin/python3
def safe_print_integer_err(value):
    """Print an integer"""
    import sys
    try:
        print("{:d}".format(value))
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return False
    else:
        return True
