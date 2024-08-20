#!/usr/bin/env python3
"""0. Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if  key or item:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
        