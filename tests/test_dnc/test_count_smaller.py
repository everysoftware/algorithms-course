from typing import Any

import pytest

from src.g_dnc.count_smaller import count_smaller_bisect, count_smaller_merge


@pytest.mark.parametrize("func", [count_smaller_bisect, count_smaller_merge])
@pytest.mark.parametrize(
    ("a", "expected"),
    [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
        ([1, 2, 3, 4], [0, 0, 0, 0]),
        ([4, 3, 2, 1], [3, 2, 1, 0]),
        ([6, 5, 4, 3, 2, 1], [5, 4, 3, 2, 1, 0]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
    ],
)
def test_count_smaller(func: Any, a: list[int], expected: list[int]) -> None:
    assert func(a) == expected


# @pytest.mark.parametrize(
#     "a, expected",
#     [
#         ([2, 3, 9, 2, 9], 2),  # (2, 2) и (3, 2)
#         ([1, 20, 6, 4, 5], 5),  # (20, 6), (20, 4), (20, 5), (6, 4), (6, 5)
#         ([1, 2, 3, 4, 5], 0),
#         ([5, 4, 3, 2, 1], 10),
#         ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
#         ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 45),
#         ([1, 3, 5, 2, 4, 6], 3),
#         ([1, 2, 3, 4, 5, 6], 0),
#         ([6, 5, 4, 3, 2, 1], 15),
#     ],
# )
# def test_count_inverse(a: list[int], expected: int) -> None:
#     assert count_inverse(a) == expected
