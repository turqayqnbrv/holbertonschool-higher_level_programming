#!/usr/bin/python3
"""Module containing VerboseList class that extends built-in list."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Append an item to the list with notification.

        Args:
            item: The item to append.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable with notification.

        Args:
            iterable: An iterable of items to add.
        """
        num_items = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        """Remove an item from the list with notification.

        Args:
            item: The item to remove.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at the given index with notification.

        Args:
            index: The index of the item to remove (default: -1 for last item).

        Returns:
            The removed item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
