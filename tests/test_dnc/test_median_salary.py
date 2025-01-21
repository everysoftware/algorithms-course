import pytest

from src.i_dnc.median_salary import median_salary


@pytest.mark.parametrize(
    "scores, expected",
    [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5, 6], 3.5),
        ([1], 1),
        ([1, 1, 1, 1], 1),
        ([5, 3, 4, 2, 1], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
        ([5, 1, 3, 2, 4], 3),
        ([4, 2, 1, 3], 2.5),
    ],
)
def test_competition(scores: list[int], expected: float):
    assert median_salary(scores) == expected
