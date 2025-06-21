from functools import partial
from typing import Any

import pytest

from src.m_trees.is_bst import is_bst, is_bst_naive
from src.m_trees.is_general_bst import is_general_bst_dfs, is_general_bst_fake

r"""
Tree 1:
     2
    / \
   1   3

Tree 2:
    1
   / \
  2   3

Tree 3:
        1
       /
      2
     /
    3
   /
  4
 /
5
"""

METHODS = ["preorder", "inorder", "preorder-iter", "inorder-iter"]
NON_NAIVE_FUNCS = [partial(is_bst, method=method) for method in METHODS]


@pytest.mark.parametrize("func", [is_general_bst_dfs, is_bst_naive, *NON_NAIVE_FUNCS])
@pytest.mark.parametrize(
    ("nodes", "expected"),
    [
        (
            [
                (2, 1, 2),
                (1, -1, -1),
                (3, -1, -1),
            ],
            True,
        ),
        (
            [
                (1, 1, 2),
                (2, -1, -1),
                (3, -1, -1),
            ],
            False,
        ),
        (
            [],
            True,
        ),
        (
            [
                (1, -1, 1),
                (2, -1, 2),
                (3, -1, 3),
                (4, -1, 4),
                (5, -1, -1),
            ],
            True,
        ),
        (
            [
                (4, 1, 2),
                (2, 3, 4),
                (6, 5, 6),
                (1, -1, -1),
                (3, -1, -1),
                (5, -1, -1),
                (7, -1, -1),
            ],
            True,
        ),
        (
            [
                (4, 1, -1),
                (2, 2, 3),
                (1, -1, -1),
                (5, -1, -1),
            ],
            False,
        ),
        (
            [
                (2, 1, 2),
                (2, -1, -1),
                (3, -1, -1),
            ],
            False,
        ),
    ],
)
def test_is_bst(func: Any, nodes: list[tuple[int, int, int]], expected: bool) -> None:
    result = func(nodes)
    assert result is expected


@pytest.mark.parametrize(
    ("nodes", "expected"),
    [
        (
            [
                (2, 1, 2),
                (1, -1, -1),
                (2, -1, -1),
            ],
            (True, False),
        ),
        (
            [
                (4, 1, 2),
                (1, -1, 3),
                (5, -1, -1),
                (2, -1, 4),
                (3, 5, -1),
                (2, -1, -1),
            ],
            (True, False),
        ),
    ],
)
def test_is_general_bst(nodes: list[tuple[int, int, int]], expected: tuple[bool, bool]) -> None:
    assert is_general_bst_dfs(nodes) is expected[0]
    assert is_bst(nodes) is expected[1]


@pytest.mark.parametrize(
    ("nodes", "expected"),
    [
        (
            # Хотя это не BST, сортировка по ключам дает правильный порядок и мы получаем ложный ответ.
            [
                (2, -1, 1),
                (5, 2, -1),
                (3, -1, 3),
                (5, -1, -1),
            ],
            True,
        ),
    ],
)
def test_is_general_bst_fake(nodes: list[tuple[int, int, int]], expected: bool) -> None:
    result = is_general_bst_fake(nodes)
    assert result is expected
