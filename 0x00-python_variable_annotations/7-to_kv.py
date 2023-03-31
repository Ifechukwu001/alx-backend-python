#!/usr/bin/env python3
"""Module to create tuple
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Create a tuple

    Args:
        k (str): First.
        v (int | float): Second.

    Returns:
        tuple(str, float): Output.
    """
    return (k, v * v)
