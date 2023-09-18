#!/usr/bin/python3
# test_rectangle.py

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    /* Add similar test methods for three, four, and five args */

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    # Add similar test methods for private attributes and getters/setters

class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_valid_width_types(self):
        valid_widths = [10, "10", 5.5, complex(5), True, [1, 2, 3], {1, 2, 3}, (1, 2, 3), frozenset({1, 2, 3}), range(5)]
        for width in valid_widths:
            with self.subTest(width=width):
                r = Rectangle(width, 1)
                self.assertEqual(r.width, int(widt))

class TestRectangleStrAndDisplay(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    def test_str_method_print_width_height(self):
        r = Rectangle(4, 6)
        capture = self.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    @staticmethod
    def capture_stdout(rect, method):
