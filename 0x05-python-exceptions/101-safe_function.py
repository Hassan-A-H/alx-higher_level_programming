#!/usr/bin/python3
def safe_function(fct, *args):
    """Executes a function safely"""
    import sys
    try:
        result = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        result = None

    return (result)
