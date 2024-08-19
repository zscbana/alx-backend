#!/usr/bin/env python3
"""1. Simple pagination"""
import csv
from typing import List, Tuple
import math


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size 'page_size' of the 'page'"""
    Start_index = (page - 1) * page_size
    End_index = page_size + Start_index
    return (Start_index, End_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        start_index, End_index = index_range(page, page_size)

        return data[start_index:End_index]
