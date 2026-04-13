#!/usr/bin/python3
"""Test script for Task 1 - Shapes with Duck Typing."""

from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

print("Circle:")
shape_info(circle)
print("\nRectangle:")
shape_info(rectangle)
