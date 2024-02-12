from typing import Callable

import pytest

from base_ds.application import tree_height_naive, tree_height_stack


@pytest.mark.parametrize("f", [tree_height_naive, tree_height_stack])
@pytest.mark.parametrize(
    "tree, expected",
    [
        ([4, -1, 4, 1, 1], 3),
        ([-1, 0, 4, 0, 3], 4),
        ([9, 7, 5, 5, 2, 9, 9, 9, 2, -1], 4),
        (
            [
                2,
                8,
                -1,
                8,
                3,
                1,
                2,
                5,
                5,
                7,
                7,
                0,
                0,
                5,
                5,
                2,
                3,
                0,
                0,
                2,
                0,
                0,
                8,
                8,
                2,
                2,
                2,
            ],
            3,
        ),
    ],
)
def test_tree_height(
    f: Callable[[list[int]], int], tree: list[int], expected: int
) -> None:
    assert f(tree) == expected
