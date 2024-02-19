import pytest

from searches import lower_bound, upper_bound


@pytest.mark.parametrize(
    "a, target, expected",
    [
        # Возрастающая последовательность
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, 5),
        ([1, 2, 3, 4, 5], 0, 0),
        ([1, 3, 5, 7, 9], 6, 3),
        ([1, 3, 5, 7, 9], 10, 5),
        # Неубывающая последовательность
        ([1, 1, 2, 2, 3, 3], 2, 2),
        ([1, 1, 2, 2, 3, 3], 4, 6),
        # Повторяющийся элемент
        ([1, 1, 1, 1, 1], 1, 0),
        # Одноэлементная последовательность
        ([1], 1, 0),
    ],
)
def test_lower_bound(a: list[int], target: int, expected: int):
    assert lower_bound(a, target) == expected


@pytest.mark.parametrize(
    "a, target, expected",
    [
        # Убывающая последовательность
        ([9, 7, 5, 3, 1], 6, 2),
        ([9, 7, 5, 3, 1], 0, 5),
        # Невозрастающая последовательность
        ([5, 5, 4, 4, 3, 3], 4, 2),
        ([5, 5, 4, 4, 3, 3], 2, 6),
    ],
)
def test_lower_bound_decreasing(a: list[int], target: int, expected: int):
    assert lower_bound(a, -target, key=lambda x: -x) == expected


@pytest.mark.parametrize(
    "a, target, expected",
    [
        # Возрастающая последовательность
        ([1, 2, 3, 4, 5], 3, 3),
        ([1, 2, 3, 4, 5], 1, 1),
        ([1, 2, 3, 4, 5], 5, 5),
        ([1, 2, 3, 4, 5], 6, 5),
        ([1, 2, 3, 4, 5], 0, 0),
        # Неубывающая последовательность
        ([1, 1, 2, 2, 3, 3], 2, 4),
        ([1, 1, 2, 2, 3, 3], 4, 6),
        # Повторяющийся элемент
        ([1, 1, 1, 1, 1], 1, 5),
        # Одноэлементная последовательность
        ([1], 1, 1),
    ],
)
def test_upper_bound(a: list[int], target: int, expected: int):
    assert upper_bound(a, target) == expected


@pytest.mark.parametrize(
    "a, target, expected",
    [
        # Убывающая последовательность
        ([9, 7, 5, 3, 1], 6, 2),
        ([9, 7, 5, 3, 1], 0, 5),
        # Невозрастающая последовательность
        ([5, 5, 4, 4, 3, 3], 4, 4),
        ([5, 5, 4, 4, 3, 3], 2, 6),
    ],
)
def test_upper_bound_decreasing(a: list[int], target: int, expected: int):
    assert upper_bound(a, -target, key=lambda x: -x) == expected
