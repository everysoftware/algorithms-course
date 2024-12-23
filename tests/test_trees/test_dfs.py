from typing import Any

import pytest

from src.trees.dfs import dfs, dfs_iterative

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}
"""
      A
    /   \
    B     C
   / \   / \
  D   E F   G
"""


@pytest.mark.parametrize("impl", [dfs])
def test_dfs(impl: Any) -> None:
    assert impl(tree, "A") == ["A", "B", "D", "E", "C", "F", "G"]
    assert impl(tree, "B") == ["B", "D", "E"]
    assert impl(tree, "C") == ["C", "F", "G"]
    assert impl(tree, "D") == ["D"]
    assert impl(tree, "E") == ["E"]
    assert impl(tree, "F") == ["F"]
    assert impl(tree, "G") == ["G"]


@pytest.mark.parametrize("impl", [dfs_iterative])
def test_dfs_iterative(impl: Any) -> None:
    assert impl(tree, "A") == ["A", "C", "G", "F", "B", "E", "D"]
    assert impl(tree, "B") == ["B", "E", "D"]
    assert impl(tree, "C") == ["C", "G", "F"]
    assert impl(tree, "D") == ["D"]
    assert impl(tree, "E") == ["E"]
    assert impl(tree, "F") == ["F"]
    assert impl(tree, "G") == ["G"]
