from functools import wraps


def log_action(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{message}] {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator
