from typing import Callable

import pytest

from searches import binary_search, lower_bound, upper_bound, exp_search


@pytest.mark.parametrize("f", [binary_search, exp_search])
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
    f: Callable[[list[int], int], int], a: list[int], target: int, expected: int
):
    assert f(a, target) == expected


@pytest.mark.parametrize(
    "f, a, target, expected",
    [
        (binary_search, [1, 1, 1, 1, 1], 1, 2),
        (exp_search, [1, 1, 1, 1, 1], 1, 3),
    ],
)
def test_repeating_sequence(
    f: Callable[[list[int], int], int], a: list[int], target: int, expected: int
):
    assert f(a, target) == expected


@pytest.mark.parametrize(
    "a, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, 5),
        ([1, 2, 3, 4, 5], 0, 0),
        ([1, 1, 1, 1, 1], 1, 0),
        ([1], 1, 0),
    ],
)
def test_lower_bound(a: list[int], target: int, expected: int):
    assert lower_bound(a, target) == expected


@pytest.mark.parametrize(
    "a, target, expected",
    [
        ([1, 2, 3, 4, 5], 3, 3),
        ([1, 2, 3, 4, 5], 1, 1),
        ([1, 2, 3, 4, 5], 5, 5),
        ([1, 2, 3, 4, 5], 6, 5),
        ([1, 2, 3, 4, 5], 0, 0),
        ([1, 1, 1, 1, 1], 1, 5),
        ([1], 1, 1),
    ],
)
def test_upper_bound(a: list[int], target: int, expected: int):
    assert upper_bound(a, target) == expected
