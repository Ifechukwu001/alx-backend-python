#!/usr/bin/env python3
"""Async comprehensions

"""
import asyncio
import typing
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """The comprehension function

    Returns:
        list of floats: The random numbers.
    """
    numbers = [num async for num in async_generator()]
    return numbers
