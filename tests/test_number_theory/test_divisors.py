from collections.abc import Callable

import pytest

from src.h_number_theory.divisors import closest_divisors, divisors_naive, divisors_sqrt


@pytest.mark.parametrize("func", [divisors_naive, divisors_sqrt])
@pytest.mark.parametrize(
    "x, expected",
    [
        (1, False),  # [1]
        (2, False),  # [1, 2]
        (3, False),  # [1, 3]
        (4, True),  # [1, 2, 4]
        (5, False),  # [1, 5]
        (6, False),  # [1, 2, 3, 6]
        (7, False),  # [1, 7]
        (8, False),  # [1, 2, 4, 8]
        (9, True),  # [1, 3, 9]
        (10, False),  # [1, 2, 5, 10]
        (11, False),  # [1, 11]
        (12, False),  # [1, 2, 3, 4, 6, 12]
        (13, False),  # [1, 13]
        (14, False),  # [1, 2, 7, 14]
        (15, False),  # [1, 3, 5, 15]
        (16, False),  # [1, 2, 4, 8, 16]
        (17, False),  # [1, 17]
        (18, False),  # [1, 2, 3, 6, 9, 18]
        (19, False),  # [1, 19]
        (20, False),  # [1, 2, 4, 5, 10, 20]
    ],
)
def test_three_divisors(func: Callable[[int], list[int]], x: int, expected: list[int]) -> None:
    assert func(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (8, [3, 3]),  # 9 = 3 * 3
        (123, [5, 25]),  # 125 = 5 * 25
        (999, [25, 40]),  # 1000 = 40 * 25
    ],
)
def test_closest_divisors(x: int, expected: list[int]) -> None:
    assert closest_divisors(x) == expected
