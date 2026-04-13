#!/usr/bin/python3
"""Test script for Task 0 - Abstract Animal Class."""

from task_00_abc import Animal, Dog, Cat

# Test Dog and Cat
bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

# Test that Animal cannot be instantiated
try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print(f"TypeError: {e}")
