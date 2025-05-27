# pyratelimit

A simple decorator-based rate limiter for Python. Limits how often a function can be called within a given time window. Useful for small scripts, tools, or development environments where basic rate limiting is needed.

## Installation

Copy the `rate_limiter.py` file into your project

</n>

No external dependencies. Only uses the Python standard library.

## Usage Example

```python
from rate_limiter import rate_limit, RateLimitExceeded

@rate_limit(calls=3, period=60)
def my_function():
    print("Function called")

for i in range(5):
    try:
        my_function()
    except RateLimitExceeded as e:
        print(e)
```

This example allows the function to run 3 times per 60 seconds. The 4th and 5th calls raise an exception.

</n>

You can also use a key_func to apply rate limits per user:

```python
@rate_limit(calls=2, period=10, key_func=lambda user_id: f"user:{user_id}")
def do_action(user_id):
    print(f"Action for {user_id}")
```

## API

### `rate_limit(calls: int, period: int, key_func: Optional[Callable] = None)`

Decorator that limits how often a function can be called.

- `calls`: number of allowed calls
- `period`: time window in seconds
- `key_func`: optional function that returns a unique key based on arguments. Defaults to the function name.

### `RateLimitExceeded(Exception)`

Raised when a function is called more than allowed during the period.

## Notes

- This component is not persistent — it resets when the process stops.
- It is not distributed — works in a single process/threaded app.
- Thread-safe via locking.

## License

MIT License — you can use, copy, and modify it freely.
