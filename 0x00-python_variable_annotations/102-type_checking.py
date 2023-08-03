#!/usr/bin/env python3
"""
function for zooming in on a tuple
"""
from typing import Tuple, List


def zoom_array(lst: Tuple[int], factor: int = 2) -> List[int]:
    """
    Returns:
         a list
    """
    zoomed_in: List[int] = [
        item for item in list(lst)
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
