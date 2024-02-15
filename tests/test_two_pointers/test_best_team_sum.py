import pytest

from two_pointers import best_team_sum


@pytest.mark.parametrize(
    "a, expected", [([1, 3, 5, 7, 9], 21), ([1, 2, 3, 4, 5], 14), ([1, 1, 1, 1, 1], 5)]
)
def test_best_team_sum(a: list[int], expected: int):
    assert best_team_sum(a) == expected
