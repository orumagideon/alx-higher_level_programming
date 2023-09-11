#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square, a special case of a rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size (side length) of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
