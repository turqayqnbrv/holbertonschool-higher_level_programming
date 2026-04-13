#!/usr/bin/python3
"""This module is used to define MyList class"""


class MyList(list):
    """This class inherits from list type"""

    def print_sorted(self):
        """Prints the elements of the list in ascending order"""
        print(sorted(self))
