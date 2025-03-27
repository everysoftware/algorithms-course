from collections.abc import Callable

import pytest

from src.f_scanline import (
    count_segments,
    count_segments_bisect,
)


@pytest.mark.parametrize("func", [count_segments_bisect, count_segments])
@pytest.mark.parametrize(
    ("segments", "points", "expected"),
    [
        # Тест 1: Проверка на массиве с одним отрезком и одной точкой
        ([(1, 5)], [3], [1]),
        # Тест 2: Проверка на массиве с несколькими отрезками и одной точкой
        ([(1, 5), (2, 6), (3, 7)], [4], [3]),
        # Тест 3: Проверка на массиве с несколькими отрезками и несколькими точками
        ([(1, 5), (2, 6), (3, 7)], [4, 6, 1, 7], [3, 2, 1, 1]),
        # Тест 4: Проверка на массиве с несколькими отрезками и точками вне отрезков
        ([(1, 5), (2, 6), (3, 7)], [0, 8], [0, 0]),
        ([(0, 5), (7, 10)], [1, 6, 11], [1, 0, 0]),
        ([(0, 5), (7, 10)], [0, 5, 7, 10], [1, 1, 1, 1]),
        ([(0, 5), (7, 10)], [0, 1, 5, 6, 7, 10, 11], [1, 1, 1, 0, 1, 1, 0]),
    ],
)
def test_points_and_segments(
    func: Callable[[list[tuple[int, int]], list[int]], list[int]],
    segments: list[tuple[int, int]],
    points: list[int],
    expected: list[int],
) -> None:
    assert func(segments, points) == expected
