from typing import Callable

import pytest

from src.h_number_theory.array_gcd import gcd_naive, gcd_euclid, gcd_euclid_rec


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (18, 35, 1),
        (10, 20, 5),
        (100, 200, 50),
    ],
)
def test_gcd_naive(a: int, b: int, expected: int) -> None:
    assert gcd_naive(a, b) == expected


@pytest.mark.parametrize("func", [gcd_euclid, gcd_euclid_rec])
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (28851538, 1183019, 17657),
        (14159572, 63967072, 4),
    ],
)
def test_gcd_huge(func: Callable[[int, int], int], a: int, b: int, expected: int) -> None:
    assert func(a, b) == expected
