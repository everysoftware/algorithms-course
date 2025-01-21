import pytest

from src.k_dp import ladder


@pytest.mark.parametrize(
    "a, expected",
    [
        ([1, 2], 3),
        ([2, -1], 1),
        ([-1, 2, 1], 3),
        ([-2, -16, -13, -9, -48], -63),
        ([1, 1, -2, -4, -6, 2, 2], 2),
        ([-64, -16, -13, -9, -48], -73),
        ([3, 4, 10, 10, 0, -6, -10, 0], 21),
        ([-100, -1000], -1000),
    ],
)
def test_ladder(a: list[int], expected: int):
    assert ladder(a) == expected
