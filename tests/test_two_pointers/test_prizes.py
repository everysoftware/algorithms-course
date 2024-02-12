import pytest

from two_pointers.implementation import prizes


@pytest.mark.parametrize(
    "prize_positions, k, expected",
    [
        ([1, 1, 2, 2, 3, 3, 5], 2, 6),
        ([1, 1, 2, 2, 3, 3, 5], 1, 4),
        ([1, 1, 2, 2, 3, 3, 5], 4, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 4),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 1),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], 9, 10),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], 8, 9),
        ([], 5, 0),
    ],
)
def test_prizes(prize_positions: list[int], k: int, expected: int):
    assert prizes(prize_positions, k) == expected
