from typing import Callable

import pytest

from number_theory import divisors_naive, divisors


@pytest.mark.parametrize("func", [divisors_naive, divisors])
@pytest.mark.parametrize(
    "x, expected",
    [
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 3]),
        (4, [1, 2, 4]),
        (5, [1, 5]),
        (6, [1, 2, 3, 6]),
        (7, [1, 7]),
        (8, [1, 2, 4, 8]),
        (9, [1, 3, 9]),
        (10, [1, 2, 5, 10]),
        (11, [1, 11]),
        (12, [1, 2, 3, 4, 6, 12]),
        (13, [1, 13]),
        (14, [1, 2, 7, 14]),
        (15, [1, 3, 5, 15]),
        (16, [1, 2, 4, 8, 16]),
        (17, [1, 17]),
        (18, [1, 2, 3, 6, 9, 18]),
        (19, [1, 19]),
        (20, [1, 2, 4, 5, 10, 20]),
        (21, [1, 3, 7, 21]),
        (22, [1, 2, 11, 22]),
        (23, [1, 23]),
        (24, [1, 2, 3, 4, 6, 8, 12, 24]),
        (25, [1, 5, 25]),
    ],
)
def test_is_prime(
    func: Callable[[int], list[int]], x: int, expected: list[int]
) -> None:
    assert func(x) == expected
