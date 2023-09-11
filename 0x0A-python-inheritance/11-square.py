#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
from typing import Union
from .9-rectangle import Rectangle  # Adjust the import path based on your project structure.

class Square(Rectangle):
    """Represents a square, a special case of a rectangle."""

    def __init__(self, size: int):
        """Initialize a new Square.

        Args:
            size (int): The size (side length) of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
