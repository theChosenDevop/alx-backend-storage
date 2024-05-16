#!/usr/bin/env python3
"""
    Exercise module
"""
import redis
import uuid
from typing import Union, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None)
    -> Union[str, bytes, int, float, None]:
        """Returns the value"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """Returns a converted string"""
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: int) -> Union[int, None]:
        """Returns a converted integer"""
        return self.get(key, fn=int)
