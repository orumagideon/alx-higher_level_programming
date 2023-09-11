#!/usr/bin/python3
"""inherited list class MyList."""

class MyList(list):
    """Implementation of sorted printing for the built-in list class."""

    def print_sorted(self):
        """list in sorted ascending order."""
        print(sorted(self))
