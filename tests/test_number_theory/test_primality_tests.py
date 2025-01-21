import pytest

from src.h_number_theory.primality_tests import primality_tests


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
