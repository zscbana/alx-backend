#!/usr/bin/env python3
"""1. FIFO caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFO caching class"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache Using FIFO"""
        if key or item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
