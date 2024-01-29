#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if a_dictionary is None:
        return (None)
    else:
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[max]:
                max = key
        return (max)
