from typing import Callable

import pytest

from src.dp2 import lcs_rec, lcs_dp


@pytest.mark.parametrize(
    "func",
    [
        lcs_rec,
        lcs_dp,
    ],
)
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("AGGTAB", "GXTXAYB", 4),  # Стандартные кейсы
        ("ABCBDAB", "BDCAB", 4),
        ("ABCDGH", "AEDFHR", 3),
        ("", "", 0),  # Пустые строки
        ("A", "A", 1),  # Одинаковые строки
        ("A", "B", 0),  # Разные строки
    ],
)
def test_lcs(func: Callable[[str, str], int], a: str, b: str, expected: int):
    assert func(a, b) == expected
