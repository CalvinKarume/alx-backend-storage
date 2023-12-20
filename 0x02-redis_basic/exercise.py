#!/usr/bin/env python3
"""writing strings to redis"""
from typing import Callable, Optional
from functools import wraps
import redis
import uuid


class cache:
    """A class cache using redis"""
    def __init__(self):
        """initialize the cache by creating a redis client
        and flushing the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def count_calls(method: Callable) -> Callable:
        """Read from redis"""
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """wrapper function"""
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper

    def call_history(method: Callable) -> Callable:
        """Decorator to store the history of inputs and outputs"""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """wrapper function"""
            inputt = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", inputt)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input data in Redis with a randomly generated key
        and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """Retrieve data from the cache using the provided key"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve a string from the cache"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Retrieve an integer from the cache"""
        return self.get(key, int)

    def replay(self, method: Callable):
        """Display the history of calls for a particular method"""
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")

        for args, output in zip(inputs, outputs):
            print(f"{method.__qualname__}{args} -> {output}")
