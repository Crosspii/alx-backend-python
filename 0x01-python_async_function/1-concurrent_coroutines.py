#!/usr/bin/env python3
"""Concurrent coroutine that spawns wait_random n times."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay and return list of delays
    in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    results = []
    for completed_task in asyncio.as_completed(delays):
        result = await completed_task
        results.append(result)

    return results
