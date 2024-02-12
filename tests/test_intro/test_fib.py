from typing import Callable

import pytest

from intro.implementation import (
    fib_rec,
    fib_cache,
    fib_dp,
    fib_two_last,
    fib_mod_two_last,
    fib_mod_pisano,
    fib_formula,
)


@pytest.mark.parametrize("f", [fib_rec, fib_cache, fib_dp, fib_two_last, fib_formula])
@pytest.mark.parametrize(
    ["n", "expected"], zip([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 1, 2, 3, 5, 8, 13, 21, 34])
)
def test_fib(f: Callable[[int], int], n: int, expected: int):
    assert f(n) == expected


@pytest.mark.parametrize(
    "f",
    [
        fib_cache,
        fib_dp,
        fib_two_last,
    ],
)
@pytest.mark.parametrize(
    ["n", "expected"],
    zip([10, 20, 30, 40, 100], [55, 6765, 832040, 102334155, 354224848179261915075]),
)
def test_fib_huge(f: Callable[[int], int], n: int, expected: int):
    assert f(n) == expected


@pytest.mark.parametrize(
    "f",
    [
        fib_mod_two_last,
        fib_mod_pisano,
    ],
)
@pytest.mark.parametrize(
    ["n", "m", "expected"],
    [
        (10, 2, 1),
        (50, 13, 5),
    ],
)
def test_fib_mod(f: Callable[[int, int], int], n: int, m: int, expected: int):
    assert f(n, m) == expected


@pytest.mark.parametrize(
    "f",
    [
        fib_mod_pisano,
    ],
)
@pytest.mark.parametrize(
    ["n", "m", "expected"],
    [
        (60282445765134413, 2263, 974),
    ],
)
def test_fib_mod_huge(f: Callable[[int, int], int], n: int, m: int, expected: int):
    assert f(n, m) == expected
