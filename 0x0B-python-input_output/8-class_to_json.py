#!/usr/bin/python3
"""Function Defines Python class-to-JSON function."""


def class_to_json(obj):
    """Dictionary represntation of a simple data structure."""
    return obj.__dict__
