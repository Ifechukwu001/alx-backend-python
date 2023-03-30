#!/usr/bin/env python3
"""Module creating a multiplier decorator
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Multiplier decorator
    
    Args:
        multiplier (float): Multiplier value.
        
    Returns:
        function: Output.
    """
    return lambda x: x * multiplier
