import pytest

from src.prefix_sums import unfinished_tasks


@pytest.mark.parametrize(
    "a, requests, expected",
    [
        # Тест 1: Проверка на пустом массиве
        ([], [], []),
        # Тест 2: Проверка на массиве без нулей
        ([1, 1, 1, 1], [(1, 4)], [0]),
        # Тест 3: Проверка на массиве только с нулями
        ([0, 0, 0, 0], [(1, 4)], [4]),
        # Тест 4: Проверка на массиве с нулями и ненулевыми числами
        ([1, 0, 0, 1, 0, 1, 0, 1], [(1, 3), (2, 5), (3, 7)], [2, 3, 3]),
        # Тест 5: Проверка на массиве с нулями и ненулевыми числами, где L = R
        ([1, 0, 0, 1, 0, 1, 0, 1], [(3, 3)], [1]),
    ],
)
def test_unfinished_tasks(a: list[int], requests: list[tuple[int, int]], expected: list[int]):
    assert unfinished_tasks(a, requests) == expected
