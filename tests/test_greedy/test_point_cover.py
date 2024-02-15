from typing import Callable

import pytest

from greedy import points_cover, points_cover_enhanced


@pytest.mark.parametrize("f", [points_cover, points_cover_enhanced])
@pytest.mark.parametrize(
    "points, expected",
    [
        ([1, 2, 3, 4, 5], [(1, 2), (3, 4), (5, 6)]),
        ([0.5, 2, 1, 3.5, 10, 0.7, 1.2], [(0.5, 1.5), (2, 3), (3.5, 4.5), (10, 11)]),
        (
            [4.5, 3, 6.2, 2, 9, 14.2, 1.2, 4, 8.7],
            [(1.2, 2.2), (3, 4), (4.5, 5.5), (6.2, 7.2), (8.7, 9.7), (14.2, 15.2)],
        ),
    ],
)
def test_point_cover(
    f: Callable[[list[float]], list[tuple[float, float]]],
    points: list[float],
    expected: list[tuple[float, float]],
):
    assert f(points) == expected
