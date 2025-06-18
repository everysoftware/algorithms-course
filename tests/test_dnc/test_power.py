from typing import Any

import pytest

from src.g_dnc.power import fast_power


@pytest.mark.parametrize(
    "func",
    [fast_power],
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
        (123, 987),
        (2.1, 3),
        (2, -2),
    ],
)
def test_power(func: Any, x: float, y: int) -> None:
    assert func(x, y) == x**y
