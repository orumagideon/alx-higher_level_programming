#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
from typing import Union
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)  # Validate width as an integer.
        self.__width = width
        super().integer_validator("height", height)  # Validate height as an integer.
        self.__height = height

    def area(self) -> int:
        """Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """Return a string representation of the Rectangle.

        Returns:
            str: A string representation in the format "[Rectangle] width/height".
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
