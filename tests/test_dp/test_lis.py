import pytest

from dp import lis


@pytest.mark.parametrize(
    "a, expected",
    [
        ([0, 7, 1, 6, 2], [0, 1, 2]),  # Пример из задания
        ([10, 9, 2, 5, 3, 7, 101, 18], [2, 3, 7, 18]),  # Пример из LeetCode
        (
            [0, 1, 0, 3, 2, 3],
            [0, 1, 2, 3],
        ),  # Возрастающая подпоследовательность
        ([7, 7, 7, 7, 7], [7]),  # Все элементы одинаковые
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1]),  # Убывающая последовательность
    ],
)
def test_lis(a: list[int], expected: list[int]):
    assert lis(a) == expected
