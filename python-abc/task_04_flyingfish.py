#!/usr/bin/python3
"""Module containing Fish, Bird, and FlyingFish classes."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish (multiple inheritance)."""

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print that the flying fish is flying."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")
