#!/usr/bin/env python3
"""1. Simple pagination"""
import csv
from typing import List, Dict
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
        """Get a page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        start_index, End_index = index_range(page, page_size)

        if start_index > len(data):
            return []

        return data[start_index:End_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get a page of the dataset"""
        page_data = self.get_page(page, page_size)
        start_index, End_index = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if End_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
