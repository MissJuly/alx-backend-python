#!/usr/bin/env python3
"""
Import async_comprehension from the previous file
and write a measure_runtime coroutine that will
execute async_comprehension 4 times in parallel
using asyncio.gather
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns:
        float: the runtime of the async_comprehension function in seconds
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
