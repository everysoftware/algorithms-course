from typing import Any

import pytest

from src.b_base_ds import sliding_window_naive, sliding_window_deque


@pytest.mark.parametrize("func", [sliding_window_naive, sliding_window_deque])
@pytest.mark.parametrize(
    "m, a, expected",
    [
        (4, [2, 7, 3, 1, 5, 2, 6, 2], [7, 7, 5, 6, 6]),
        (3, [2, 1, 5, 3, 4, 6, 7], [5, 5, 5, 6, 7]),
        (4, [2, 1, 5, 3, 4, 6, 7], [5, 5, 6, 7]),
        (1, [2, 1, 5, 3, 4, 6, 7], [2, 1, 5, 3, 4, 6, 7]),
        (7, [2, 1, 5, 3, 4, 6, 7], [7]),
        (7, [7, 6, 5, 4, 3, 2, 1], [7]),
        (7, [1, 2, 3, 4, 5, 6, 7], [7]),
    ],
)
def test_sliding_window(
    func: Any,
    m: int,
    a: list[int],
    expected: list[int],
):
    assert func(len(a), a, m) == expected
