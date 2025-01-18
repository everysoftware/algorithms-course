import pytest

from src.two_pointers.can_trasform import can_transform


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
def test_can_transform(a: str, b: str, expected: bool) -> None:
    assert can_transform(a, b) == expected
