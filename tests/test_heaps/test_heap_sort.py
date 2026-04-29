from collections.abc import Callable

import pytest

from src.heaps.heap_sort import heap_sort, heap_sort_inplace


@pytest.mark.parametrize(
    "func",
    [
        heap_sort,
        heap_sort_inplace,
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
def test_heap_sort(func: Callable[[list[int]], list[int] | None], a: list[int]) -> None:
    a = a.copy()
    result = func(a)
    expected = sorted(a)

    if result is None:
        assert a == expected
    else:
        assert result == expected
