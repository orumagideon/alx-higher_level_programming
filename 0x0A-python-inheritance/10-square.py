#!/usr/bin/python3
"""Defines a Square subclass of Rectangle."""
from typing import Union
from .9-rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a special case of a rectangle."""

    def __init__(self, size: int):
        """Initialize a new square.

        Args:
            size (int): The size (side length) of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
