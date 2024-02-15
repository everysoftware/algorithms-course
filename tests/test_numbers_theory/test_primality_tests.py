import pytest

from numbers_theory import primality_tests, decompose


@pytest.mark.parametrize(
    "n, expected",
    [
        (18, (9, 1)),
        (20, (5, 2)),
        (32, (1, 5)),
        (100, (25, 2)),
    ],
)
def test_decompose(n, expected):
    assert decompose(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (8273, ([517, 7755], 8272)),
        (97, ([3, 93], 96)),
        (13, ([3, 9], 12)),
        (15, ([1, 1], 4)),
    ],
)
def test_primality_tests(n: int, expected: tuple[list[int], int]) -> None:
    assert primality_tests(n) == expected
