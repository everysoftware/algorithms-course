import random
from typing import Callable

import pytest

from dp2 import coins_path, coins_recursive, coins_cache, coins_dp


def generate_field() -> tuple[int, int, list[list[int]]]:
    n, m = random.randint(1, 10), random.randint(1, 10)
    field = [[random.randint(-100, 100) for _ in range(m)] for _ in range(n)]
    i_start, j_start = random.randint(0, n - 1), random.randint(0, m - 1)

    return i_start, j_start, field


@pytest.mark.parametrize(
    "func",
    [
        coins_recursive,
        coins_cache,
        coins_dp,
    ],
)
@pytest.mark.parametrize(
    "i_start, j_start, coins, expected",
    [
        (0, 0, [[0, 1], [1, 0]], 1),
        (0, 0, [[0, 1, 2], [3, 4, 5], [6, 7, 8]], 24),
        (0, 0, [[0, 1, 1], [1, 1, 0]], 2),
        (0, 0, [[0, 1, 0], [1, 1, 1]], 3),
        (0, 0, [[0, 0, 0], [0, 0, 0]], 0),
        (0, 0, [[1]], 0),
    ],
)
def test_coins(
    func: Callable[[int, int, list[list[int]]], int],
    i_start: int,
    j_start: int,
    coins: list[list[int]],
    expected: int,
):
    assert func(i_start, j_start, coins) == expected


@pytest.mark.parametrize(
    "func",
    [
        coins_cache,
        coins_dp,
    ],
)
@pytest.mark.parametrize(
    "i_start, j_start, coins", [generate_field() for _ in range(10)]
)
def test_coins_random(
    func: Callable[[int, int, list[list[int]]], int],
    i_start: int,
    j_start: int,
    coins: list[list[int]],
):
    assert func(i_start, j_start, coins) == coins_recursive(i_start, j_start, coins)


@pytest.mark.parametrize(
    "i_start, j_start, coins, expected",
    [
        (0, 0, [[0, 1], [1, 0]], (1, [(0, 0), (0, 1), (1, 1)])),
        (
            0,
            0,
            [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
            (24, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        ),
        (0, 0, [[0, 1, 1], [1, 1, 0]], (2, [(0, 0), (0, 1), (0, 2), (1, 2)])),
        (0, 0, [[0, 1, 0], [1, 1, 1]], (3, [(0, 0), (0, 1), (1, 1), (1, 2)])),
        (0, 0, [[0, 0, 0], [0, 0, 0]], (0, [(0, 0), (0, 1), (0, 2), (1, 2)])),
        (0, 0, [[1]], (0, [(0, 0)])),
    ],
)
def test_coins_path(
    i_start: int,
    j_start: int,
    coins: list[list[int]],
    expected: tuple[int, list[tuple[int, int]]],
):
    assert coins_path(i_start, j_start, coins) == expected
