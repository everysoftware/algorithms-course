from collections.abc import Callable

import pytest

from src.g_dnc.multiply import mul_dnc, mul_karatsuba, mul_naive


@pytest.mark.parametrize(
    "func",
    [mul_naive, mul_dnc, mul_karatsuba],
)
@pytest.mark.parametrize(
    ("x", "y"),
    [
        (0, 0),
        (1, 1),
        (1, 0),
        (0, 1),
        (2, 2),
        (2, 3),
        (3, 2),
        (10, 10),
        (10, 11),
        (11, 10),
        (10, 100),
        (100, 10),
        (123456789, 987654321),
        (123456789, 9876543210),
        (1234567890, 987654321),
        (1234567890, 9876543210),
        (9874563256487921, 152458796389852357456),
    ],
)
def test_multiply(func: Callable[[int, int], int], x: int, y: int) -> None:
    assert func(x, y) == x * y
