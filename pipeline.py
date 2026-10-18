"""Pipeline обработки данных."""
from typing import Callable, Any
from functools import reduce

def pipeline(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Возвращает функцию, применяющую functions последовательно слева направо."""
    def apply(value: Any) -> Any:
        return reduce(lambda acc, func: func(acc), functions, value)
    return apply

if __name__ == "__main__":
    process = pipeline(
        lambda nums: filter(lambda x: x % 2 == 0, nums),
        lambda nums: map(lambda x: x ** 2, nums),
        lambda nums: sum(nums)
    )
    print(process(range(1, 11)))  # 4+16+36+64+100 = 220