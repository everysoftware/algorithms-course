from typing import Callable

import pytest

from intro import gcd_naive, gcd_euclid, gcd_euclid_rec


@pytest.mark.parametrize("f", [gcd_naive, gcd_euclid, gcd_euclid_rec])
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (18, 35, 1),
        (14159572, 63967072, 4),
    ],
)
def test_gcd(f: Callable[[int, int], int], a: int, b: int, expected: int):
    assert f(a, b) == expected
