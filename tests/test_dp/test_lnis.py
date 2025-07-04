import pytest

from src.h_dp.lnis import lnis


@pytest.mark.parametrize(
    ("a", "expected"),
    [
        ([0, 7, 1, 6, 2], [7, 6, 2]),
        ([8, 4, 4, 2], [8, 4, 4, 2]),
        ([3, 6, 2], [6, 2]),
        ([0, 3, 1, 6, 2, 2, 7], [6, 2, 2]),
        ([1], [1]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 2, 3, 4], [4]),
        ([4, 3, 2, 1], [4, 3, 2, 1]),
    ],
)
def test_lnis(a: list[int], expected: list[int]) -> None:
    assert lnis(a) == expected
