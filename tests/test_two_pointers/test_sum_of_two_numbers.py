from typing import Callable

import pytest

from two_pointers.implementation import (
    sum_of_two_numbers_tp,
    sum_of_two_numbers_naive,
)


@pytest.mark.parametrize(
    "f",
    [
        sum_of_two_numbers_naive,
        sum_of_two_numbers_tp,
    ],
)
@pytest.mark.parametrize(
    "arr, target, expected",
    [
        [[2, 7, 11, 15], 9, (0, 1)],
        [[2, 3, 4], 6, (0, 2)],
        [[3, 3], 6, (0, 1)],
    ],
)
def test_sum_of_two_numbers(
    f: Callable[[list[int], int], tuple[int, int]],
    arr: list[int],
    target: int,
    expected: tuple[int, int],
):
    assert f(arr, target) == expected