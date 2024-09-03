from typing import Callable

import pytest

from src.search import binary_search, exp_search


@pytest.mark.parametrize("func", [binary_search, exp_search])
@pytest.mark.parametrize(
    "a, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([1, 2, 3, 4, 5], 0, -1),
        ([1], 1, 0),
    ],
)
def test_searches(
    func: Callable[[list[int], int], int],
    a: list[int],
    target: int,
    expected: int,
):
    assert func(a, target) == expected


@pytest.mark.parametrize(
    "func, a, target, expected",
    [
        (binary_search, [1, 1, 1, 1, 1], 1, 2),
        (exp_search, [1, 1, 1, 1, 1], 1, 3),
    ],
)
def test_repeating_sequence(
    func: Callable[[list[int], int], int],
    a: list[int],
    target: int,
    expected: int,
):
    assert func(a, target) == expected
