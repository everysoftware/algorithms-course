from typing import Any

import pytest

from src.two_pointers.shortest_palindrome import shortest_naive, shortest_kmp


@pytest.mark.parametrize("func", [shortest_naive, shortest_kmp])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("aacecaaa", "aaacecaaa"),
        ("abcd", "dcbabcd"),
        ("a", "a"),
        ("ab", "bab"),
        ("abc", "cbabc"),
        ("abac", "cabac"),
        ("abacaba", "abacaba"),
    ],
)
def test_shortest_palindrome(func: Any, s: str, expected: str) -> None:
    assert func(s) == expected
