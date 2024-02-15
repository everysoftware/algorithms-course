from typing import Callable

import pytest

from prefix import max_subsequence_sum_naive, max_subsequence_sum_ps


@pytest.mark.parametrize(
    "f",
    [
        max_subsequence_sum_naive,
        max_subsequence_sum_ps,
    ],
)
@pytest.mark.parametrize(
    "d, a, expected",
    [
        (1000, [997, 3, 4, 12, 88, 1900], 2000),
    ],
)
def test_max_subsequence_sum_easy(
    f: Callable[[int, list[int]], int], d: int, a: list[int], expected: int
):
    assert f(d, a) == expected


@pytest.mark.parametrize(
    "file, expected",
    [
        ("2900-A.txt", 259000),
    ],
)
def test_max_subsequence_sum_naive(file: str, expected: int):
    with open(f"../tests/data/{file}") as f:
        d, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

    assert max_subsequence_sum_naive(d, a) == expected


@pytest.mark.parametrize(
    "file, expected",
    [
        ("2900-A.txt", 259000),
        ("2900-B.txt", 49763000),
    ],
)
def test_max_subsequence_sum_ps(file: str, expected: int):
    with open(f"../tests/data/{file}") as f:
        d, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

    assert max_subsequence_sum_ps(d, a) == expected
