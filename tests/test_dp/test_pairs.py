import random
from typing import Callable

import pytest

from dp import pairs_naive, pairs_dp, pairs_dp_imperfect


@pytest.mark.parametrize("func", [pairs_naive, pairs_dp_imperfect, pairs_dp])
@pytest.mark.parametrize(
    "d, a, expected",
    [
        (10, [2, 13, 15, 4, 10, 6, 6], 2),
    ],
)
def test_pairs_sample(
    func: Callable[[int, list[int]], int], d: int, a: list[int], expected: int
):
    assert func(d, a) == expected


@pytest.mark.parametrize("func", [pairs_dp_imperfect, pairs_dp])
@pytest.mark.parametrize(
    "d, a",
    [
        (random.randint(2, 1000), [random.randint(1, 1000) for _ in range(300)])
        for _ in range(10)
    ],
)
def test_pairs_random(func: Callable[[int, list[int]], int], d: int, a: list[int]):
    assert func(d, a) == pairs_naive(d, a)


@pytest.mark.parametrize("func", [pairs_naive, pairs_dp_imperfect, pairs_dp])
@pytest.mark.parametrize(
    "path, expected",
    [
        ("../tests/data/226-A.txt", 15),
    ],
)
def test_pairs_a(func: Callable[[int, list[int]], int], path: str, expected: int):
    with open(path) as f:
        d, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

        assert func(d, a) == expected


@pytest.mark.parametrize("func", [pairs_dp_imperfect, pairs_dp])
@pytest.mark.parametrize(
    "path, expected",
    [
        ("../tests/data/226-B.txt", 5001021),
    ],
)
def test_pairs_b(func: Callable[[int, list[int]], int], path: str, expected: int):
    with open(path) as f:
        d, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

        assert func(d, a) == expected
