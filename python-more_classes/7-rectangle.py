#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area."""
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Str Representation."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = []
        for i in range(self.__height):
            rect_lines.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Reproduction string."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
