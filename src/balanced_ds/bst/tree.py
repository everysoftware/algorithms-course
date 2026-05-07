from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Literal, Self, overload

from src.balanced_ds.base.node import K, Node, V
from src.balanced_ds.base.tree import BinaryTree
from src.balanced_ds.base.utils import get_node_key
from src.balanced_ds.bst.node import BSTNode
from src.balanced_ds.bst.operations import (
    R,
    bst_delete,
    bst_find,
    bst_insert,
    bst_max,
    bst_merge,
    bst_min,
    bst_next,
    bst_order_statistics,
    bst_prev,
    bst_split,
    dfs,
)
from src.balanced_ds.bst.utils import (
    bst_visualize,
    check_attributes,
    check_for_cycles,
    check_parents,
    is_bst,
    update_attributes_recursive,
)

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence


class BST(BinaryTree[K, V]):
    node_type: ClassVar[type[BSTNode[Any, Any]]] = BSTNode

    @classmethod
    def from_keys(cls, keys: Sequence[K] = ()) -> Self:
        bst = cls()
        for key in keys:
            bst.insert(key)
        return bst

    @classmethod
    def from_array(cls, arr: Sequence[tuple[K, int, int] | list[Any]]) -> Self:
        size = len(arr)
        tree = [cls.node_type(0) for _ in range(size)]

        for i in range(size):
            key, left_idx, right_idx = arr[i]
            tree[i].key = key

            if left_idx >= 0:
                node = tree[left_idx]
                tree[i].left = node
                node.parent = tree[i]

            if right_idx >= 0:
                node = tree[right_idx]
                tree[i].right = node
                node.parent = tree[i]

        if tree:
            root = tree[0]
            update_attributes_recursive(root)
        else:
            root = None

        return cls(root)

    def empty(self) -> bool:
        """Проверка дерева на пустоту"""
        return self.root is None

    def insert(self, key: K, value: V | None = None) -> Node[K, V]:
        """Вставка узла в дерево по ключу и значению"""
        self.root = bst_insert(self.root, self.node_type, key, value=value)
        return self.root

    def find(self, key: K) -> Node[K, V] | None:
        """Поиск узла по ключу"""
        return bst_find(self.root, key)

    def contains(self, key: K) -> bool:
        """Проверка наличия узла в дереве по ключу"""
        return self.find(key) is not None

    def delete(self, key: K) -> Node[K, V] | None:
        """Удаление узла из дерева по ключу"""
        self.root = bst_delete(self.root, key)
        return self.root

    def max(self) -> Node[K, V] | None:
        """Поиск узла с максимальным ключом"""
        return bst_max(self.root)

    def min(self) -> Node[K, V] | None:
        """Поиск узла с минимальным ключом"""
        return bst_min(self.root)

    def next(self, key: K) -> Node[K, V] | None:
        """Поиск узла, следующего за данным"""
        node = self.find(key)
        assert node is not None
        return bst_next(node)

    def prev(self, key: K) -> Node[K, V] | None:
        """Поиск узла, предшествующего данному"""
        node = self.find(key)
        assert node is not None
        return bst_prev(node)

    @overload
    def dfs(
        self,
        *,
        node: Node[K, V] | None = None,
        style: Literal["inorder", "preorder", "postorder"] = "inorder",
        key: Callable[[Node[Any, Any]], K] = get_node_key,
    ) -> list[K]: ...

    @overload
    def dfs(
        self,
        *,
        node: Node[K, V] | None = None,
        style: Literal["inorder", "preorder", "postorder"] = "inorder",
        key: Callable[[Node[Any, Any]], R],
    ) -> list[R]: ...

    def dfs(
        self,
        *,
        node: Node[K, V] | None = None,
        style: Literal["inorder", "preorder", "postorder"] = "inorder",
        key: Callable[[Node[Any, Any]], R] = get_node_key,
    ) -> list[R]:
        """Обход дерева в глубину (DFS)"""
        root = self.root if node is None else node
        return dfs(root, style, key)

    def order_statistics(self, k: int) -> Node[K, V] | None:
        """Порядковая статистика"""
        return bst_order_statistics(self.root, k)

    def split(self, key: K) -> tuple[Self, Self]:
        """Разбиение дерева на 2 дерева: (left <= key < right). На месте."""
        left, right = bst_split(self.root, key)
        return self.__class__(root=left), self.__class__(root=right)

    def merge(self, rhs: Self) -> Self:
        """Слияние двух деревьев. На месте."""
        self.root = bst_merge(self.root, rhs.root)
        return self

    def check_correctness(self) -> Self:
        """Проверка корректности дерева"""
        check_for_cycles(self.root)
        check_parents(self.root)
        check_attributes(self.root)

        assert is_bst(self.root)

        return self

    def __str__(self) -> str:
        """Представление дерева в виде строки"""
        result = f"{type(self).__name__} ({self.root})\n"
        result += "Nodes: "
        result += str(dfs(self.root)) + "\n"
        result += bst_visualize(self.root)

        return result

    def __repr__(self) -> str:
        """Представление дерева"""
        return str(self)
