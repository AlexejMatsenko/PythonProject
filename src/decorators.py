import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор логирует имя функции и результат выполнения операции,
    так же при ошибке и входные параметры."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{func.__name__}: ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> Any:
    """Функция вычесляет результат деления двух чисел"""
    return x / y


@log()
def my_function1(x: int, y: int) -> Any:
    return x / y


my_function(4, 0)
my_function(4, 2)
my_function(
    4,
)
