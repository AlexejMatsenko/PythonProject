from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_information = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_information + "\n")
                else:
                    print(log_information)
                return result
            except Exception as e:
                log_information = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_information + "\n")
                else:
                    print(log_information)
                raise

        return wrapper

    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(4, 2)