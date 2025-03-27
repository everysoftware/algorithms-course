from collections.abc import Callable

import pytest

from src.e_two_pointers.two_sum import (
    two_sum_naive,
    two_sum_tp,
)


@pytest.mark.parametrize(
    "func",
    [
        two_sum_naive,
        two_sum_tp,
    ],
)
@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, (0, 7)),
        ([2, 7, 11, 15], 9, (0, 1)),
        ([2, 3, 4], 6, (0, 2)),
        ([3, 3], 6, (0, 1)),
    ],
)
def test_sum_of_two_numbers(
    func: Callable[[list[int], int], tuple[int, int]],
    arr: list[int],
    target: int,
    expected: tuple[int, int],
):
    assert func(arr, target) == expected
