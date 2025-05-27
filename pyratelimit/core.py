import time
import threading
from functools import wraps

class RateLimitExceeded(Exception):
    pass

class InMemoryStore:
    def __init__(self):
        self.lock = threading.Lock()
        self.calls = {}

    def is_allowed(self, key, limit, period):
        now = time.time()
        with self.lock:
            timestamps = self.calls.get(key, [])
            timestamps = [t for t in timestamps if t > now - period]
            if len(timestamps) >= limit:
                return False
            timestamps.append(now)
            self.calls[key] = timestamps
            return True

store = InMemoryStore()

def rate_limit(calls: int, period: int, key_func=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = key_func(*args, **kwargs) if key_func else func.__name__
            if not store.is_allowed(key, calls, period):
                raise RateLimitExceeded(f"Rate limit exceeded for key: {key}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
