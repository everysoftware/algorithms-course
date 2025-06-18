from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None


# O(n)
def dfs_all(nodes: list[tuple[int, int, int]]) -> tuple[list[int], list[int], list[int]]:
    """
    Perform DFS on a tree represented by a list of tuples (key, left_index, right_index).
    Returns three lists: inorder, preorder, and postorder traversals.
    """
    root = build_tree(nodes)
    return (
        dfs_inorder(root),
        dfs_preorder(root),
        dfs_postorder(root),
    )


# O(n)
def dfs(root: Node, style: Literal["inorder", "preorder", "postorder"] = "inorder") -> list[int]:
    """
    Perform DFS on a tree and return the traversal in the specified style.
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
def dfs_inorder(node: Node | None) -> list[int]:
    """
    Perform an inorder DFS traversal of the tree.
    """
    if node is None:
        return []
    # dfs_inorder(node.left) + [node.key] + dfs_inorder(node.right)
    return [*dfs_inorder(node.left), node.key, *dfs_inorder(node.right)]


# O(n)
def dfs_preorder(node: Node | None) -> list[int]:
    """
    Perform a preorder DFS traversal of the tree.
    """
    if node is None:
        return []
    # [node.key] + dfs_preorder(node.left) + dfs_preorder(node.right)
    return [node.key, *dfs_preorder(node.left), *dfs_preorder(node.right)]


# O(n)
def dfs_postorder(node: Node | None) -> list[int]:
    """
    Perform a postorder DFS traversal of the tree.
    """
    if node is None:
        return []
    # dfs_postorder(node.left) + dfs_postorder(node.right) + [node.key]
    return dfs_postorder(node.left) + dfs_postorder(node.right) + [node.key]


# O(n)
def build_tree(nodes: list[tuple[int, int, int]]) -> Node:
    """
    Build a binary tree from a list of tuples where each tuple contains:
    - key: the value of the node
    - left_index: index of the left child (-1 if no left child)
    - right_index: index of the right child (-1 if no right child)
    """
    n = len(nodes)
    if n <= 0:
        raise ValueError("Input list must contain at least one element.")
    tree = [Node(0) for _ in range(n)]
    for i in range(n):
        key, left, right = nodes[i]
        tree[i].key = key
        if left >= 0:
            tree[i].left = tree[left]
        if right >= 0:
            tree[i].right = tree[right]
    return tree[0]


# Advanced: Iterative DFS implementation


# O(n)
def dfs_all_iterative(nodes: list[tuple[int, int, int]]) -> tuple[list[int], list[int], list[int]]:
    """
    Perform an iterative DFS on a tree represented by a list of tuples (key, left_index, right_index).
    Returns three lists: inorder, preorder, and postorder traversals.
    """
    root = build_tree(nodes)
    return (
        dfs_inorder_iterative(root),
        dfs_preorder_iterative(root),
        dfs_postorder_iterative(root),
    )


# O(n)
def dfs_preorder_iterative(node: Node) -> list[int]:
    """
    Perform an iterative preorder DFS traversal of the tree.
    """
    st = [node]
    result = []
    while st:
        node = st.pop()
        result.append(node.key)
        # Push right first so that left is processed first
        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)
    return result


# O(n)
def dfs_postorder_iterative(node: Node) -> list[int]:
    """
    Perform an iterative postorder DFS traversal of the tree.
    """
    st = [node]
    result = []
    while st:
        node = st.pop()
        result.append(node.key)
        # Push left first so that right is processed first
        if node.left is not None:
            st.append(node.left)
        if node.right is not None:
            st.append(node.right)
    # Reverse the result to get postorder
    result.reverse()
    return result


# O(n)
def dfs_inorder_iterative(node: Node) -> list[int]:
    """
    Perform an iterative inorder DFS traversal of the tree.
    """
    st: list[Node] = []
    result: list[int] = []
    curr: Node | None = node
    while st or curr is not None:
        # Go to the leftmost node
        if curr is not None:
            st.append(curr)
            curr = curr.left
        # Process the node
        else:
            # Pop from stack and visit the node
            curr = st.pop()
            result.append(curr.key)
            curr = curr.right
    return result
