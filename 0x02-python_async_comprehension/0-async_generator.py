#!/usr/bin/env python3
"""Async Generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async Generator
    """
    for count in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
