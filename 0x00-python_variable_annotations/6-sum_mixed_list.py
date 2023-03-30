#!/usr/bin/env python3
"""Module containing mixed list
"""
import typing

def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """Sums inputs
    
    Args:
        mxd_list (int | float): Input data.
        
    Returns:
        float: Sum.
    """
    return float(sum(mxd_list))
