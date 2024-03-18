#!/usr/bin/env python3
"""Let's execute multiple coroutines at
the same time with async
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute wait_random n times with the specified max_delay.
    Args:
        @n: int
        @max_delay: int
    return:
        @List[float]
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
