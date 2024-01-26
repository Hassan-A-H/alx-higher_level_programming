#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character."""

    lens = len(sentence)
    if lens == 0:
        return (0, None)
    else:
        return (lens, sentence[0])
