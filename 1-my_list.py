#!/usr/bin/python

"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints the list sorted in ascending sort"""
        print(sorted(self))
