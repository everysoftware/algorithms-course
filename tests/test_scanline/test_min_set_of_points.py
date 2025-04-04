import pytest

from src.f_scanline.min_set_of_points import min_set_of_points


@pytest.mark.parametrize(
    ("segments", "expected"),
    [
        ([(1, 3), (2, 5), (3, 6)], [3]),
        ([(4, 7), (1, 3), (2, 5), (5, 6)], [3, 6]),
        ([(1, 2), (2, 5), (5, 6)], [2, 6]),
        ([(1, 2), (2, 3), (3, 4), (4, 5)], [2, 4]),
    ],
)
def test_min_set_of_points(segments: list[tuple[int, int]], expected: list[int]) -> None:
    assert min_set_of_points(segments) == expected
