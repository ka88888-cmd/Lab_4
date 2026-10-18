"""Квадраты чисел 1–10 с помощью map."""
from typing import List

def squares_1_to_10() -> List[int]:
    """Возвращает список квадратов чисел от 1 до 10."""
    return list(map(lambda x: x ** 2, range(1, 11)))

if __name__ == "__main__":
    print(squares_1_to_10())