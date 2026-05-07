"""
Продвинутые операции с АВЛ-деревом
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from src.balanced_ds.base.attributes import Height
from src.balanced_ds.bst.operations import bst_delete_child, bst_max, bst_merge_with_root, bst_prev, clear_parent

if TYPE_CHECKING:
    from src.balanced_ds.base.node import NodeT


def get_balance(node: NodeT | None) -> int:
    """
    Коэффициент сбалансированности k:
    если k <= 1, то всё хорошо,
    если k = -2, значит, слева высота больше, поэтому балансируем дерево вправо,
    если k = 2, значит, больше высота справа, и нужно балансировать дерево влево.
    """
    if node is None:
        return 0

    return Height.value(node.right) - Height.value(node.left)


def right_rotate(node: NodeT) -> NodeT:
    # node = 4
    node_parent = node.parent  # ...
    a = node.left  # 2
    assert a is not None
    b = a.right  # 3
    a.right = node
    node.parent = a
    node.left = b

    if b is not None:
        b.parent = node

    a.parent = node_parent

    if a.parent is not None:
        if a.parent.left is node:
            a.parent.left = a
        else:
            a.parent.right = a

    node.update()

    if a is not None:
        a.update()

    return a


def left_rotate(node: NodeT) -> NodeT:
    # node = 4
    node_parent = node.parent  # ...
    a = node.right  # 2
    assert a is not None
    b = a.left  # 3
    a.left = node
    node.parent = a
    node.right = b

    if b is not None:
        b.parent = node

    a.parent = node_parent

    if a.parent is not None:
        if a.parent.left is node:
            a.parent.left = a
        else:
            a.parent.right = a

    node.update()

    if a is not None:
        a.update()

    return a


def balance(node: NodeT | None) -> NodeT | None:
    if node is None:
        return None

    node.update()
    k = get_balance(node)
    possible_new_root = node

    if k == -2:
        if get_balance(node.left) == 1:
            assert node.left is not None
            left_rotate(node.left)
        possible_new_root = right_rotate(node)
    elif k == 2:
        if get_balance(node.right) == -1:
            assert node.right is not None
            right_rotate(node.right)
        possible_new_root = left_rotate(node)

    return possible_new_root


def avl_insert(
    node: NodeT | None,
    node_type: type[NodeT],
    key: Any,
    *,
    value: Any = None,
    parent: NodeT | None = None,
) -> NodeT:
    if node is None:
        return node_type(key, value, parent=parent)

    if node.key > key:
        node.left = avl_insert(node.left, node_type, key, value=value, parent=node)
    elif node.key < key:
        node.right = avl_insert(node.right, node_type, key, value=value, parent=node)

    node = balance(node)
    assert node is not None
    return node


def avl_delete(node: NodeT | None, key: Any) -> NodeT | None:
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
            node.left = avl_delete(node.left, swap_node.key)
    elif node.key > key:
        node.left = avl_delete(node.left, key)
    else:
        node.right = avl_delete(node.right, key)

    return balance(node)


def avl_merge_with_root(left: NodeT | None, right: NodeT | None, root: NodeT | None) -> NodeT | None:
    """Склейка при известной идеально подходящей вершине root: (node1 < root <= node2)."""
    if root is None:
        return None

    h1 = Height.value(left)
    h2 = Height.value(right)

    if abs(h1 - h2) <= 1:
        bst_merge_with_root(left, right, root)

        return balance(root)
    elif h1 > h2:
        assert left is not None
        new_root = avl_merge_with_root(left.right, right, root)
        assert new_root is not None
        left.right = new_root
        new_root.parent = left

        return balance(left)
    else:
        assert right is not None
        new_root = avl_merge_with_root(left, right.left, root)
        assert new_root is not None
        right.left = new_root
        new_root.parent = right

        return balance(right)


def avl_merge(left: NodeT | None, right: NodeT | None) -> NodeT | None:
    """Слияние двух АВЛ-деревьев."""
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    new_root = bst_max(left)
    assert new_root is not None
    left = avl_delete(left, new_root.key)
    clear_parent(new_root)

    return avl_merge_with_root(left, right, new_root)


def avl_split(node: NodeT | None, key: Any) -> tuple[NodeT | None, NodeT | None]:
    """Разделение АВЛ-дерева по ключу."""
    if node is None:
        return None, None

    if node.key > key:
        left, temp = avl_split(node.left, key)
        clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        temp, right = avl_split(node.right, key)
        clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)

    clear_parent(left, right)

    return left, right
