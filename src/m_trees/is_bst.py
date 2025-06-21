from typing import Literal

from src.m_trees.dfs import BNode, build_tree
from src.m_trees.dfs_iterative import dfs_iterative

INF = 10**20


# O(n log n)
def is_bst_naive(nodes: list[tuple[int, int, int]]) -> bool:
    if not nodes:
        return True
    expected_keys = sorted(x[0] for x in nodes)
    if len(expected_keys) != len(set(expected_keys)):
        return False
    root = build_tree(nodes)
    actual_keys = dfs_iterative(root)
    return actual_keys == expected_keys


# O(n)
def is_bst(
    nodes: list[tuple[int, int, int]],
    method: Literal["preorder", "inorder", "preorder-iter", "inorder-iter"] = "inorder-iter",
) -> bool:
    if not nodes:
        return True
    root = build_tree(nodes)
    match method:
        case "preorder":
            return is_bst_preorder(root)
        case "inorder":
            return is_bst_inorder(root)
        case "preorder-iter":
            return is_bst_preorder_iterative(root)
        case "inorder-iter":
            return is_bst_inorder_iterative(root)
        case _:
            raise ValueError(f"Unknown method: {method}")


# O(n)
def is_bst_preorder(node: BNode | None, min_key: int = -INF, max_key: int = INF) -> bool:
    if node is None:
        return True
    # Проверяем, что ключ текущего узла находится в допустимом диапазоне.
    # Если ключ меньше минимального или больше максимального, то это не BST.
    # not(min_key <= node.key <= max_key)
    if node.key < min_key or node.key > max_key:
        return False
    # Рекурсивно проверяем левое и правое поддерево.
    # Левое поддерево должно содержать ключи меньше текущего узла,
    # а правое поддерево - ключи больше текущего узла.
    return is_bst_preorder(node.left, min_key, node.key - 1) and is_bst_preorder(node.right, node.key + 1, max_key)


# O(n)
def is_bst_inorder(node: BNode | None, prev: list[int] | None = None) -> bool:
    if node is None:
        return True
    # Используем список для хранения предыдущего узла, чтобы сохранять его между рекурсивными вызовами.
    if prev is None:
        prev = [-INF]
    # Проверяем левое поддерево: все ключи должны быть меньше текущего узла.
    is_left_correct = is_bst_inorder(node.left, prev)
    # Значение текущего узла должно быть больше предыдущего.
    if node.key <= prev[0]:
        return False
    # Обновляем значение предыдущего узла.
    prev[0] = node.key
    # Обновляем данные предыдущего узла и проверяем правое поддерево.
    return is_left_correct and is_bst_inorder(node.right, prev)


# O(n)
def is_bst_preorder_iterative(node: BNode) -> bool:
    st: list[tuple[BNode | None, int, int]] = [(node, -INF, INF)]
    while st:
        curr, min_key, max_key = st.pop()
        if curr is None:
            continue
        # Проверяем, что ключ текущего узла находится в допустимом диапазоне.
        # # not(min_key <= curr.key <= max_key)
        if curr.key < min_key or curr.key > max_key:
            return False
        # Добавляем правое и левое поддерево в стек.
        st.append((curr.right, curr.key + 1, max_key))
        st.append((curr.left, min_key, curr.key - 1))
    return True


# O(n)
def is_bst_inorder_iterative(node: BNode) -> bool:
    st: list[BNode] = []
    curr: BNode | None = node
    prev_key = -INF
    while st or curr is not None:
        # Переходим к левому поддереву.
        while curr is not None:
            st.append(curr)
            curr = curr.left
        # Извлекаем узел из стека.
        curr = st.pop()
        # Проверяем, что ключ текущего узла больше предыдущего.
        if curr.key <= prev_key:
            return False
        # Обновляем значение предыдущего узла.
        prev_key = curr.key
        # Переходим к правому поддереву.
        curr = curr.right
    return True
