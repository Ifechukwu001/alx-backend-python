#!/usr/bin/env python3
"""Module containing async coroutine

"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random time

    Args:
        max_delay (int): Maximum delay time

    Returns:
        float: delayed time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
