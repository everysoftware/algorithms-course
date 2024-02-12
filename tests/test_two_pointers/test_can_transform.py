import pytest

from two_pointers.implementation import can_transform


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("aba", "abb", True),  # замена
        ("aba", "ab", True),  # удаление
        ("aba", "abaa", True),  # вставка
        ("", "", True),
        ("hello", "hello", True),
        ("hello", "world", False),
        ("apple", "pie", False),
        ("pie", "apple", False),
    ],
)
def test_can_transform(a: str, b: str, expected: bool):
    assert can_transform(a, b) == expected
