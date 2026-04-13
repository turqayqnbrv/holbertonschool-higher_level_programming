#!/usr/bin/python3
"""Module that contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of, or if object is an instance
    of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
