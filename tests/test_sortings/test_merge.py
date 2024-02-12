import pytest

from sortings.implementation import merge


@pytest.mark.parametrize(
    ["a", "b", "expected"],
    [
        [[1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]],
        [[1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]],
        [[1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]],
        [[1, 2, 3], [], [1, 2, 3]],
        [[], [1, 2, 3], [1, 2, 3]],
        [[], [], []],
        [[-3, -2, -1], [1, 2, 3], [-3, -2, -1, 1, 2, 3]],
        [[1, 1, 2, 2, 3, 3], [2, 2, 3, 3, 4, 4], [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4]],
    ],
)
def test_merge(a: list[int], b: list[int], expected: list[int]):
    assert merge(a, b) == expected
