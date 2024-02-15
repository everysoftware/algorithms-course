from typing import Callable

import pytest

from prefix import count_subsequence_ps, count_subsequence_naive


@pytest.mark.parametrize(
    "f",
    [
        count_subsequence_naive,
        count_subsequence_ps,
    ],
)
@pytest.mark.parametrize(
    "k, a, expected",
    [
        (117, [108, 129, 143, 186, 72, 195, 94, 38, 69], 3),
    ],
)
def test_subsequence_count(
    f: Callable[[int, list[int]], int], k: int, a: list[int], expected: int
):
    assert f(k, a) == expected


@pytest.mark.parametrize(
    "file, expected",
    [
        ("2363-A.txt", 34),
    ],
)
def test_subsequence_count_naive(file: str, expected: int):
    with open(f"../tests/data/{file}") as f:
        k, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

    assert count_subsequence_naive(k, a) == expected


@pytest.mark.parametrize(
    "file, expected",
    [
        ("2363-A.txt", 34),
        ("2363-B.txt", 42729434),
    ],
)
def test_subsequence_count_ps(file: str, expected: int):
    with open(f"../tests/data/{file}") as f:
        k, _ = list(map(int, f.readline().split()))
        a = [int(x) for x in f]

    assert count_subsequence_ps(k, a) == expected
