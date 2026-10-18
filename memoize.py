"""Декоратор мемоизации."""
from functools import wraps
from typing import Callable, Any, Dict, Tuple

def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """Кэширует результаты функции по аргументам."""
    cache: Dict[Tuple[Any, ...], Any] = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache  # type: ignore
    return wrapper

@memoize
def fib(n: int) -> int:
    """Числа Фибоначчи с мемоизацией."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(10))  # 55
    print(f"Кэш: {fib.cache}")