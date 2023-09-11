#!/usr/bin/python3
"""Defines a Square class, a special case of Rectangle."""

from .9_rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special case of a rectangle."""

    def __init__(self, size: int):
        """Initialize a new square.

        Args:
            size (int): The side length of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
