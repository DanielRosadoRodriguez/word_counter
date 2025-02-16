from typing import Iterable
import abc

my_global_var = 3

def sum_even_numbers(numbers: Iterable[int]) -> int:
    """Given an iterab
    le of integers, return the sum of all even numbers in the iterable."""
    return sum(
        num for num in numbers
        if num % 2 == 0
    )

class MyClass:
    def do_thing():
        pass