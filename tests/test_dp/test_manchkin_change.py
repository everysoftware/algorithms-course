import pytest

from src.dp import manchkin_change


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 1),
        (4, 2),
        (5, 1),
        (6, 2),
        (7, 3),
        (8, 2),
        (9, 3),
        (10, 1),
        (4242, 426),
    ],
)
def test_manchkin_change(n: int, expected: int):
    assert manchkin_change(n) == expected
