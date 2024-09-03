import pytest

from src.sorting import count_inverse


@pytest.mark.parametrize(
    "a, expected",
    [
        ([2, 3, 9, 2, 9], 2),  # (2, 2) и (3, 2)
        ([1, 20, 6, 4, 5], 5),  # (20, 6), (20, 4), (20, 5), (6, 4), (6, 5)
        ([1, 2, 3, 4, 5], 0),
        ([5, 4, 3, 2, 1], 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 45),
        ([1, 3, 5, 2, 4, 6], 3),
        ([1, 2, 3, 4, 5, 6], 0),
        ([6, 5, 4, 3, 2, 1], 15),
    ],
)
def test_count_inverse(a: list[int], expected: int):
    assert count_inverse(a) == expected
