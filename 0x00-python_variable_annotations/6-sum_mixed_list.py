#!/usr/bin/env python3
"""
Module for summing list values
"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns:
        float: The sum of the elements in mxd_list
    """
    return sum(mxd_list)
