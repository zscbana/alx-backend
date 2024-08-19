#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple

def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size 'page_size' of the 'page'"""
    Start_index = (page - 1) * page_size
    End_index = page_size + Start_index
    return (Start_index, End_index)
