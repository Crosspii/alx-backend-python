#!/usr/bin/env python3
""" Spawn task_wait_random n times and return list of delays."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return a list of all dealys in ascending order."""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    results = []
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        results.append(result)

    return results
