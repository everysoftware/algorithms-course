from __future__ import annotations

from typing import Any, ClassVar

from src.balanced_ds.avl.node import AVLNode
from src.balanced_ds.avl.operations import avl_delete, avl_insert, avl_merge, avl_split
from src.balanced_ds.avl.utils import check_balance
from src.balanced_ds.base.node import K, Node, V
from src.balanced_ds.bst.tree import BST


class AVLTree(BST[K, V]):
    node_type: ClassVar[type[AVLNode[Any, Any]]] = AVLNode

    def insert(self, key: K, value: V | None = None) -> Node[K, V]:
        """Вставка элемента в дерево."""
        self.root = avl_insert(self.root, self.node_type, key, value=value)
        return self.root

    def delete(self, key: K) -> Node[K, V] | None:
        """Удаление элемента из дерева."""
        self.root = avl_delete(self.root, key)
        return self.root

    def split(self, key: K) -> tuple[AVLTree[K, V], AVLTree[K, V]]:
        """Разделение дерева на два по ключу."""
        left, right = avl_split(self.root, key)
        return self.__class__(root=left), self.__class__(root=right)

    def merge(self, rhs: AVLTree[K, V]) -> AVLTree[K, V]:
        """Слияние двух деревьев."""
        self.root = avl_merge(self.root, rhs.root)
        return self

    def check_correctness(self) -> AVLTree[K, V]:
        """Проверка корректности дерева."""
        super().check_correctness()
        check_balance(self)

        return self
