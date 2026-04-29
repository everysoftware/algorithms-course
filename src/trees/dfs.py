from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass
class BNode:
    key: int
    left: BNode | None = None
    right: BNode | None = None


# O(n)
def dfs_all(nodes: list[tuple[int, int, int]]) -> tuple[list[int], list[int], list[int]]:
    """
    Обход дерева в глубину (DFS) с использованием рекурсии. Возвращает три списка:
    - inorder (симметричный) обход
    - preorder (прямой) обход
    - postorder (обратный) обход
    """
    root = build_tree(nodes)
    return (
        dfs(root, "inorder"),
        dfs(root, "preorder"),
        dfs(root, "postorder"),
    )


# O(n)
def dfs(root: BNode, style: Literal["inorder", "preorder", "postorder"] = "inorder") -> list[int]:
    """
    Обход дерева в глубину (DFS) с использованием рекурсии.
    """
    match style:
        case "inorder":
            return dfs_inorder(root)
        case "preorder":
            return dfs_preorder(root)
        case "postorder":
            return dfs_postorder(root)
        case _:
            raise ValueError(f"Unknown DFS style: {style}")


# O(n)
def dfs_inorder(node: BNode | None) -> list[int]:
    """
    Обход дерева в глубину (DFS) в симметричном порядке.
    """
    if node is None:
        return []
    # dfs_inorder(node.left) + [node.key] + dfs_inorder(node.right)
    return [*dfs_inorder(node.left), node.key, *dfs_inorder(node.right)]


# O(n)
def dfs_preorder(node: BNode | None) -> list[int]:
    """
    Обход дерева в глубину (DFS) в прямом порядке.
    """
    if node is None:
        return []
    # [node.key] + dfs_preorder(node.left) + dfs_preorder(node.right)
    return [node.key, *dfs_preorder(node.left), *dfs_preorder(node.right)]


# O(n)
def dfs_postorder(node: BNode | None) -> list[int]:
    """
    Обход дерева в глубину (DFS) в обратном порядке.
    """
    if node is None:
        return []
    # dfs_postorder(node.left) + dfs_postorder(node.right) + [node.key]
    return [*dfs_postorder(node.left), *dfs_postorder(node.right), node.key]


# O(n)
def build_tree(nodes: list[tuple[int, int, int]]) -> BNode:
    """
    Строит бинарное дерево из списка кортежей (ключ, индекс левого ребенка, индекс правого ребенка).
    -1 используется для обозначения отсутствующего ребенка.
    """
    n = len(nodes)
    if n <= 0:
        raise ValueError("Input list must contain at least one element.")
    tree = [BNode(0) for _ in range(n)]
    for i in range(n):
        key, left, right = nodes[i]
        tree[i].key = key
        if left >= 0:
            tree[i].left = tree[left]
        if right >= 0:
            tree[i].right = tree[right]
    return tree[0]
