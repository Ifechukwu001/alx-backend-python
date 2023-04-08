#!/usr/bin/env python3
"""Tasks to do

"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an async task

    Args:
        max_delay (int): Maximum delay time.

    Returns:
        :obj:`asyncio.Task`: Async task.
    """
    return asyncio.create_task(wait_random(max_delay))
