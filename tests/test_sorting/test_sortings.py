from collections.abc import Callable

import pytest

from src.d_sorting.sort_array import (
    counting_sort,
    iterative_merge_sort,
    merge_sort,
    quick_sort,
    quick_sort3,
    radix_sort,
)
from src.d_sorting.sort_colors import bubble_sort, insertion_sort, selection_sort


@pytest.mark.parametrize(
    "func",
    [
        bubble_sort,
        insertion_sort,
        selection_sort,
        quick_sort,
        quick_sort3,
        merge_sort,
        iterative_merge_sort,
        counting_sort,
        radix_sort,
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
def test_sortings(func: Callable[[list[int]], list[int] | None], a: list[int]) -> None:
    a = a.copy()
    result = func(a)
    expected = sorted(a)

    if result is None:
        assert a == expected
    else:
        assert result == expected
