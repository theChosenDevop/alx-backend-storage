#!/usr/bin/env python3
"""
    Exercise module
"""
import redis
import uuid
from typing import Union


class Cache:
    """Creates an instance of redis clients and flush the database """
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns a string output """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
