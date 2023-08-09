#!/usr/bin/env python3
"""
Test file for printing the correct output of the wait_n coroutine
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of the task objects sorted in ascending
    order by the time waited
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
