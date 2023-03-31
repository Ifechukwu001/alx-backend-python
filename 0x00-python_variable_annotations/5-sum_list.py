#!/usr/bin/env python3
"""Module containing list sum
"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Sums a list of float

    Args:
        input_list (list of float): Input data.

    Return:
        float: sum.
    """
    return sum(input_list)
