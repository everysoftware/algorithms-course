from collections.abc import Callable
from typing import Any, Literal, TypeVar

from src.balanced_ds.base.attributes import Size
from src.balanced_ds.base.node import NodeT
from src.balanced_ds.base.utils import get_node_key
from src.balanced_ds.bst.exceptions import TraverseStyleError

R = TypeVar("R")


def bst_insert(
    node: NodeT | None,
    node_type: type[NodeT],
    key: Any,
    *,
    value: Any | None = None,
    parent: NodeT | None = None,
) -> NodeT:
    if node is None:
        return node_type(key, value, parent=parent)

    if node.key > key:
        node.left = bst_insert(node.left, node_type, key, value=value, parent=node)
    elif node.key < key:
        node.right = bst_insert(node.right, node_type, key, value=value, parent=node)
    node.update()
    return node


def bst_find(node: NodeT | None, key: Any) -> NodeT | None:
    if node is None:
        return None

    if node.key == key:
        return node
    elif node.key > key:
        return bst_find(node.left, key)
    else:
        return bst_find(node.right, key)


def bst_max(node: NodeT | None) -> NodeT | None:
    if node is None:
        return None

    while node.right:
        node = node.right

    return node


def bst_min(node: NodeT | None) -> NodeT | None:
    if node is None:
        return None

    while node.left:
        node = node.left

    return node


def bst_next(node: NodeT) -> NodeT | None:
    if node.right is not None:
        return bst_min(node.right)

    # Идем наверх, пока идём направо.
    parent = node.parent
    while parent is not None and parent.right is node:
        node = parent
        parent = parent.parent

    return parent


def bst_prev(node: NodeT) -> NodeT | None:
    if node.left is not None:
        return bst_max(node.left)

    # Идем наверх, пока идём налево.
    parent = node.parent
    while parent is not None and parent.left is node:
        node = parent
        parent = parent.parent

    return parent


def bst_delete_child(node: NodeT) -> NodeT | None:
    child = node.right if node.left is None else node.left

    if child is not None:
        child.parent = node.parent

    if node.parent is not None:
        if node.parent.left is node:
            node.parent.left = child
        else:
            node.parent.right = child

    return child


def bst_delete(node: NodeT | None, key: Any) -> NodeT | None:
    if node is None:
        return None

    if node.key == key:
        if node.left is None or node.right is None:
            node = bst_delete_child(node)
        else:
            swap_node = bst_prev(node)
            assert swap_node is not None

            node.key = swap_node.key
            node.value = swap_node.value
            node.left = bst_delete(node.left, swap_node.key)
    elif node.key > key:
        node.left = bst_delete(node.left, key)
    else:
        node.right = bst_delete(node.right, key)

    if node is not None:
        node.update()

    return node


def bst_order_statistics(node: NodeT | None, k: int) -> NodeT | None:
    """Порядковая статистика в BST. Возвращает вершину с k-м по величине ключом."""
    if node is None:
        return None

    left_size = Size.value(node.left)

    if k == left_size + 1:
        return node

    if k < left_size + 1:
        return bst_order_statistics(node.left, k)
    else:
        return bst_order_statistics(node.right, k - left_size - 1)


def bst_merge_with_root(left: NodeT | None, right: NodeT | None, root: NodeT) -> NodeT:
    """Склейка при известной идеально подходящей вершине root: (node1 < root <= node2)."""
    root.left = left
    root.right = right

    if left is not None:
        left.parent = root

    if right is not None:
        right.parent = root

    root.update()

    return root


def bst_merge(left: NodeT | None, right: NodeT | None) -> NodeT | None:
    """Слияние двух BST-деревьев."""
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    new_root = bst_max(left)
    assert new_root is not None
    left = bst_delete(left, new_root.key)
    clear_parent(new_root)

    return bst_merge_with_root(left, right, new_root)


def clear_parent(*nodes: NodeT | None) -> None:
    """Удаление родителя у вершин."""
    for node in nodes:
        if node is not None:
            node.parent = None


"""
Разбиение дерева на 2 дерева: (left <= key < right).

Принцип работы:
1. Если корень больше key, то он и всё его правое поддерево должно отправиться в дерево right.
   В левом же поддереве могут быть ключи как <= key, так и > key, поэтому мы продолжаем резать его рекурсивно.

   Левая часть разреза - это сразу первая часть нашего ответа (left),
   а чтобы получить вторую часть (right) - мы сливаем правые части дерева и разреза.
2. Если корень меньше или равен key, то он и всё его левое поддерево должны отправиться в дерево left.
    В правом же поддереве могут быть как ключи <= key, так и > key, поэтому мы продолжаем резать его рекурсивно.

    Правая часть разреза - это сразу вторая часть нашего ответа (right),
    а чтобы получить первую часть (left) - мы сливаем левые части дерева и разреза.
"""


def bst_split(node: NodeT | None, key: Any) -> tuple[NodeT | None, NodeT | None]:
    """
    Разбиение дерева на 2 дерева: (left <= key < right).

    Возвращает 2 дерева: (left, right), где left - это дерево,
    в котором все ключи меньше или равны key, а right - больше key.
    """
    if node is None:
        return None, None

    if node.key > key:
        left, temp = bst_split(node.left, key)
        clear_parent(temp, node.right)
        right: NodeT | None = bst_merge_with_root(temp, node.right, node)
    else:
        temp, right = bst_split(node.right, key)
        clear_parent(node.left, temp)
        left = bst_merge_with_root(node.left, temp, node)

    clear_parent(left, right)

    return left, right


def dfs_preorder_iterative(node: NodeT | None, key: Callable[[NodeT], R] = get_node_key) -> list[R]:
    if node is None:
        return []

    st = [node]
    result = []

    while st:
        node = st.pop()

        result.append(key(node))

        if node.right is not None:
            st.append(node.right)
        if node.left is not None:
            st.append(node.left)

    return result


def dfs_inorder_iterative(node: NodeT | None, key: Callable[[NodeT], R] = get_node_key) -> list[R]:
    st: list[NodeT] = []
    result: list[R] = []

    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            result.append(key(node))
            node = node.right

    return result


def dfs_postorder_iterative(node: NodeT | None, key: Callable[[NodeT], R] = get_node_key) -> list[R]:
    if node is None:
        return []

    st = [node]
    result = []

    while st:
        node = st.pop()
        result.append(key(node))
        if node.left is not None:
            st.append(node.left)
        if node.right is not None:
            st.append(node.right)

    result.reverse()

    return result


def dfs(
    node: NodeT | None,
    style: Literal["inorder", "preorder", "postorder"] = "inorder",
    key: Callable[[NodeT], R] = get_node_key,
) -> list[R]:
    match style:
        case "inorder":
            return dfs_inorder_iterative(node, key)
        case "preorder":
            return dfs_preorder_iterative(node, key)
        case "postorder":
            return dfs_postorder_iterative(node, key)
        case _:
            raise TraverseStyleError()
