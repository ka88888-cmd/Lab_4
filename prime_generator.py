"""Генератор простых чисел."""
from typing import Generator

def is_prime(n: int) -> bool:
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator() -> Generator[int, None, None]:
    """Бесконечно генерирует простые числа."""
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

if __name__ == "__main__":
    import itertools
    print(list(itertools.islice(prime_generator(), 10)))