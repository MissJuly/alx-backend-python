#!/usr/bin/env python3
"""
Module for asychronous coroutine using asyncio
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay:int) -> List[float]:
    """
    wait for `n` random amounts of time upto `max_delay` seconds
    Returns:
        a sorted list
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
