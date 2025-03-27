from typing import Any

import pytest

from src.k_dp.length_of_lis import lis_bisect, lis_naive


@pytest.mark.parametrize("func", [lis_naive, lis_bisect])
@pytest.mark.parametrize(
    ("a", "expected"),
    [
        ([0, 7, 1, 6, 2], 3),  # [0, 1, 2]
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # [2, 3, 7, 18]
        (
            [0, 1, 0, 3, 2, 3],
            4,  # [0, 1, 2, 3],
        ),
        ([7, 7, 7, 7, 7], 1),  # [7]
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 1),  # [1]
    ],
)
def test_lis(func: Any, a: list[int], expected: int) -> None:
    assert func(a) == expected
