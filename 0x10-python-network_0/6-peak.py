#!/bin/bash
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list[int]): The list of unsorted integers.

    Returns:
        int: The index of a peak in the list.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]:
            # mid is a potential peak
            if mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]:
                return mid
            else:
                low = mid + 1
        else:
            # mid - 1 is a potential peak
            high = mid - 1
