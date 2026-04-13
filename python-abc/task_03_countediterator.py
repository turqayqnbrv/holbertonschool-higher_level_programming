#!/usr/bin/python3
"""Module containing CountedIterator class."""


class CountedIterator:
    """An iterator wrapper that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator.

        Args:
            iterable: The iterable to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item from the iterator.

        Returns:
            The next item from the wrapped iterator.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Get the number of items iterated so far.

        Returns:
            The count of items iterated.
        """
        return self.count
