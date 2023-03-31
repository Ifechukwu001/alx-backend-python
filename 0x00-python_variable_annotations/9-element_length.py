#!/usr/bin/env python3
"""Module containing element lenght
"""
import typing

def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """List elements
    
    Args:
        lst (list of sequence): Input data.
        
    Returns:
        list: Output
    """
    return [(i, len(i)) for i in lst]
