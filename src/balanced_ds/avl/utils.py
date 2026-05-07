from __future__ import annotations

from typing import TYPE_CHECKING

from src.balanced_ds.avl.exceptions import ImbalancedError
from src.balanced_ds.avl.operations import get_balance

if TYPE_CHECKING:
    from src.balanced_ds.avl.tree import AVLTree
    from src.balanced_ds.base.node import K, V


def check_balance(tree: AVLTree[K, V]) -> None:
    """Проверка сбалансированности дерева. Бросает исключение, если дерево не сбалансировано."""
    for node in tree.dfs(key=lambda _node: _node):
        balance = get_balance(node)
        if abs(balance) > 1:
            raise ImbalancedError(node, balance)
