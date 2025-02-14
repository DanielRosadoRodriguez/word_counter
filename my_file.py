from typing import Iterable

"""
lkasjfskafj
laskdfjafjl
lkasjfdkl"""


# laksfjlskafjl
def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterab
    le of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )