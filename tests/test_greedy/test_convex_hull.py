import pytest

from greedy import convex_hull


@pytest.mark.parametrize(
    "points, expected",
    [
        (
            [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)],
            [(0, 0), (0, 3), (3, 1), (4, 4)],
        ),
        (
            [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3), (5, 5)],
            [(0, 0), (0, 3), (3, 1), (5, 5)],
        ),
        ([(76, 50), (40, 14), (37, 47), (45, 20)], [(37, 47), (40, 14), (76, 50)]),
    ],
)
def test_convex_hull(points: list[tuple[int, int]], expected: list[tuple[int, int]]):
    assert convex_hull(points) == expected
