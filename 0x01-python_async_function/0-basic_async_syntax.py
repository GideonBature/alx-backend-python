#!/usr/bin/env python3
"""The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine
    param:
        @max_delay: int
    return:
        float
    """
    rand_num = random.uniform(0, max_delay)

    await asyncio.sleep(rand_num)

    return rand_num
