from collections.abc import Callable

import pytest

from src.g_prefix_sums.count_subsequences import count_subsequences_naive, count_subsequences_ps


@pytest.mark.parametrize(
    "func",
    [
        count_subsequences_naive,
        count_subsequences_ps,
    ],
)
@pytest.mark.parametrize(
    "k, a, expected",
    [
        (117, [108, 129, 143, 186, 72, 195, 94, 38, 69], 3),
    ],
)
def test_subsequence_count(func: Callable[[int, list[int]], int], k: int, a: list[int], expected: int):
    assert func(k, a) == expected


@pytest.mark.parametrize(
    "func",
    [
        count_subsequences_naive,
        count_subsequences_ps,
    ],
)
@pytest.mark.parametrize(
    "path, expected",
    [
        ("tests/data/2363-A.txt", 34),
    ],
)
def test_k_subarray_a(func: Callable[[int, list[int]], int], path: str, expected: int):
    with open(path) as f:
        k, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

    assert func(k, a) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        ("tests/data/2363-A.txt", 34),
        ("tests/data/2363-B.txt", 42729434),
    ],
)
def test_k_subarray_b(path: str, expected: int):
    with open(path) as f:
        k, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

    assert count_subsequences_ps(k, a) == expected
