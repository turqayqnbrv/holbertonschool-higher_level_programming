#!/usr/bin/python3
"""Module containing abstract Shape class and its implementations."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    try:
        print("Area: {}".format(shape.area()))
        print("Perimeter: {}".format(shape.perimeter()))
    except (AttributeError, TypeError):
        # This handles cases where the object is not a 'duck'
        return
