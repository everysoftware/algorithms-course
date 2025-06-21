from typing import Any

import pytest

from src.m_trees.dfs import dfs_all
from src.m_trees.dfs_iterative import dfs_all_iterative

r"""
Tree 1:
          0
         / \
       70   20
      /  \    \
    50   40    60
         /     /
       30    10
      /  \
    80   90

Tree 2:
        40
       /  \
     20    60
    /  \  /  \
  10  30 50  70
"""


@pytest.mark.parametrize("func", [dfs_all, dfs_all_iterative])
@pytest.mark.parametrize(
    ("nodes", "expected"),
    [
        (
            [
                (0, 7, 2),
                (10, -1, -1),
                (20, -1, 6),
                (30, 8, 9),
                (40, 3, -1),
                (50, -1, -1),
                (60, 1, -1),
                (70, 5, 4),
                (80, -1, -1),
                (90, -1, -1),
            ],
            (
                [50, 70, 80, 30, 90, 40, 0, 20, 10, 60],
                [0, 70, 50, 40, 30, 80, 90, 20, 60, 10],
                [50, 80, 90, 30, 40, 70, 10, 60, 20, 0],
            ),
        ),
        (
            [
                (40, 1, 2),
                (20, 3, 4),
                (60, 5, 6),
                (10, -1, -1),
                (30, -1, -1),
                (50, -1, -1),
                (70, -1, -1),
            ],
            ([10, 20, 30, 40, 50, 60, 70], [40, 20, 10, 30, 60, 50, 70], [10, 30, 20, 50, 70, 60, 40]),
        ),
    ],
)
def test_dfs_all(
    func: Any, nodes: list[tuple[int, int, int]], expected: tuple[list[int], list[int], list[int]]
) -> None:
    result = func(nodes)
    assert result == expected
