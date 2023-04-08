#!/usr/bin/env python3
"""Create Task that executes multiple coroutines

"""
import asyncio
import typing
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Creates Task that executes async functions

    Args:
        n (int): Number of times to all async function.
        max_delay (int): async delay.

    Returns:
        :obj:`asyncio.Task`: async task
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
