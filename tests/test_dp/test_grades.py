import pytest

from dp import grades


@pytest.mark.parametrize(
    "a, expected",
    [
        ([0, 5, 1, 6, 2], [0, 1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ],
)
def test_grades(a: list[int], expected: list[int]):
    assert grades(a) == expected
