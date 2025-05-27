from pyratelimit.core import rate_limit, RateLimitExceeded

@rate_limit(calls=3, period=10)
def do_something():
    print("Doing something")

if __name__ == "__main__":
    for i in range(5):
        try:
            do_something()
        except RateLimitExceeded as e:
            print(e)
