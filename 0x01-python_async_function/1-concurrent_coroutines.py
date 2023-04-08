#!/usr/bin/env python3
"""Executes multiple coroutines

"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """Executes async functions

    Args:
        n (int): Number of times to all async function.
        max_delay (int): async function.

    Returns:
        list of floats: List of delay times for the async functions
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
