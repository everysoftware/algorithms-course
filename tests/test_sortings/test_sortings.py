from typing import Callable

import pytest

from sortings.implementation import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    iterative_merge_sort,
    quick_sort2,
    quick_sort3,
    counting_sort,
    digit_sort,
)


def couting_sort_10(a: list[int]) -> list[int]:
    return counting_sort(a, 10)


@pytest.mark.parametrize(
    "f",
    [
        bubble_sort,
        insertion_sort,
        selection_sort,
        quick_sort2,
        quick_sort3,
        merge_sort,
        iterative_merge_sort,
        couting_sort_10,
        digit_sort,
    ],
)
@pytest.mark.parametrize(
    "a",
    [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 5, 4],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
        [5, 5, 4, 4, 3, 3, 2, 2, 1, 1],
        [1],
    ],
)
def test_sortings(f: Callable[[list[int]], list[int] | None], a: list[int]):
    result = f(a)
    expected = sorted(a)

    if result is None:
        assert a == expected
    else:
        assert result == expected
