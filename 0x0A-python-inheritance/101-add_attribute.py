#!/usr/bin/python3
"""Defines function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): Object to add an attribute to.
        att (str): Name of the attribute to add to obj.
        value (any): The value of att.

    Raises:
        AttributeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise AttributeError("can't add new attribute")
    setattr(obj, att, value)
