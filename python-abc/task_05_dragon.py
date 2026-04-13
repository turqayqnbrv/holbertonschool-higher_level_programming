#!/usr/bin/python3
"""Module containing mixin classes and Dragon class."""


class SwimMixin:
    """Mixin class that provides swimming capability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon class that combines swim and fly capabilities."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
