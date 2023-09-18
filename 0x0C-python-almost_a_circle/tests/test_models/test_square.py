#!/usr/bin/python3
"""Defines unittests for models/square.py."""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Unittests for the Square class."""

    def setUp(self):
        """Set up test cases."""
        self.s = Square(10, 2, 1, 1)

    def test_instantiation(self):
        """Test instantiation of the Square class."""
        self.assertIsInstance(self.s, Square)
        self.assertEqual(self.s.size, 10)
        self.assertEqual(self.s.x, 2)
        self.assertEqual(self.s.y, 1)
        self.assertEqual(self.s.id, 1)

    def test_area(self):
        """Test the area method."""
        self.assertEqual(self.s.area(), 100)

    def test_str_and_display_methods(self):
        """Test __str__ and display methods."""
        str_output = "[Square] (1) 2/1 - 10"
        self.assertEqual(str(self.s), str_output)
        display_output = " " * 2 + "#" * 10 + "\n" + " " * 2 + "#" * 10 + "\n"
        self.assertEqual(self.s.display(), display_output)

    def test_update_args(self):
        """Test update method with arguments."""
        self.s.update(2, 3, 4, 5)
        self.assertEqual(self.s.id, 2)
        self.assertEqual(self.s.size, 3)
        self.assertEqual(self.s.x, 4)
        self.assertEqual(self.s.y, 5)

    def test_update_kwargs(self):
        """Test update method with keyword arguments."""
        self.s.update(id=2, size=3, x=4, y=5)
        self.assertEqual(self.s.id, 2)
        self.assertEqual(self.s.size, 3)
        self.assertEqual(self.s.x, 4)
        self.assertEqual(self.s.y, 5)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        expected_dict = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(self.s.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
