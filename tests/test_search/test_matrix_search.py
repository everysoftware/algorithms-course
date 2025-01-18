import pytest

from src.search.matrix_search import ladder_search


@pytest.mark.parametrize(
    "a, target, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5, (1, 1)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9, (2, 2)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, (0, 0)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 7, (2, 0)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8, (2, 1)),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10, (-1, -1)),
    ],
)
def test_ladder_search(a: list[list[int]], target: int, expected: tuple[int, int]):
    assert ladder_search(a, target) == expected
