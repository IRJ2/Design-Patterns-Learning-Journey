import time
from functools import wraps

def retry(retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print("Attempt", attempt, "failed with error:", e)
                    if attempt == retries:
                        print(f"All {retries} attempts failed.")
                        raise
                    time.sleep(current_delay)
        return wrapper
    return decorator

def exponential_backoff(retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    print("Attempt", attempt, "failed with error:", e)
                    if attempt == retries:
                        print(f"All {retries} attempts failed.")
                        raise
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator

@exponential_backoff(retries=3, delay=1)
def make_api_request():
    import random
    if random.random() < 0.8:
        raise Exception("Network glitch!")
    return "Success!"

make_api_request()
