from typing import Callable

import pytest

from numbers_theory import is_prime, is_prime_naive


@pytest.mark.parametrize("func", [is_prime_naive, is_prime])
@pytest.mark.parametrize(
    "x, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (13, True),
        (14, False),
        (15, False),
        (16, False),
        (17, True),
        (18, False),
        (19, True),
        (20, False),
        (21, False),
        (22, False),
        (23, True),
        (24, False),
        (25, False),
    ],
)
def test_is_prime(func: Callable[[int], bool], x: int, expected: bool) -> None:
    assert func(x) == expected
