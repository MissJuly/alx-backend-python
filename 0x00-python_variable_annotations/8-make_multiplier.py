#!/usr/bin/env python3
"""
Module for creating a function that multiplies
a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns:
        Callable[[float], float]: a function that multiplies a
        float by the multiplier
    """
    def multiply(n: float) -> float:
        """
        Returns a float
        """
        return n * multiplier
    return multiply
