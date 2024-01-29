#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""

    del_item = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del_item.append(key)

    for i in del_item:
        del a_dictionary[i]

    return (a_dictionary)
