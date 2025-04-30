#!/usr/bin/env python3
""" Measures the runtime of running async_comprehenstion four times """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ run async_comprehenstion four times at the same time """
    start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return (end - start)
