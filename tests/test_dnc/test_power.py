from typing import Callable

import pytest

from dnc import power, fast_power


@pytest.mark.parametrize(
    "f",
    [power, fast_power],
)
@pytest.mark.parametrize(
    "x, y",
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
        (123, 987),
    ],
)
def test_power(f: Callable[[int, int], int], x: int, y: int) -> None:
    assert f(x, y) == x ** y
