"""Генератор случайных чисел в заданном диапазоне."""
import random
from typing import Generator

def random_numbers(start: int, end: int, count: int) -> Generator[int, None, None]:
    """Генерирует count случайных целых чисел в диапазоне [start, end]."""
    for _ in range(count):
        yield random.randint(start, end)

if __name__ == "__main__":
    print(list(random_numbers(1, 100, 5)))
