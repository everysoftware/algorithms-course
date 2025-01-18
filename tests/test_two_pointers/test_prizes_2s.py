import pytest

from src.two_pointers.prizes_2s import prizes_hard


@pytest.mark.parametrize(
    "prize_positions, k, expected",
    [
        ([1, 1, 2, 2, 3, 3, 5], 2, 7),
        ([1, 1, 2, 2, 3, 3, 5], 1, 6),
        ([1, 1, 2, 2, 3, 3, 5], 4, 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 8),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0, 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 2),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1, 2),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], 9, 10),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 10], 8, 10),
        ([], 5, 0),
    ],
)
def test_prizes_two_segments(prize_positions: list[int], k: int, expected: int):
    assert prizes_hard(prize_positions, k) == expected
