#!/usr/bin/env python3
"""Measure the runtime

"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the time to execute

    Args:
        n (int): Number of times to execute.
        max_delay (int): Maximum time to delay.

    Returns:
        float; Total average execution time.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start)/n
