from typing import Any, TypeVar

from src.balanced_ds.base.node import Node
from src.balanced_ds.bst.exceptions import CycleError, NodeAttributeError, ParentError
from src.balanced_ds.bst.operations import dfs

T = TypeVar("T")


def check_for_cycles_helper(node: Node[Any, Any] | None, visited: set[Node[Any, Any]]) -> None:
    if node is None:
        return

    if node in visited or node.parent is node:
        raise CycleError(node)

    visited.add(node)

    check_for_cycles_helper(node.left, visited)
    check_for_cycles_helper(node.right, visited)


def check_for_cycles(node: Node[Any, Any] | None) -> None:
    """Проверка наличия циклов в дереве."""
    check_for_cycles_helper(node, set())


def check_parents(node: Node[Any, Any] | None) -> None:
    """Проверка родителей узлов."""
    for _node in dfs(node, key=lambda _node: _node):
        if _node.left and _node.left.parent is not _node:
            raise ParentError("left", _node)
        if _node.right and _node.right.parent is not _node:
            raise ParentError("right", _node)


def check_attributes(node: Node[Any, Any] | None) -> None:
    """Проверка атрибутов узлов."""
    if node is None:
        return
    for attribute in node.attributes_to_update:
        for _node in dfs(node, key=lambda _node: _node):
            if not attribute.check(_node):
                raise NodeAttributeError(attribute, _node)


def is_bst(node: Node[Any, Any] | None) -> bool:
    """
    Проверка, является ли дерево строгим BST. В строгом BST каждый узел должен быть больше всех узлов
    в его левом поддереве и меньше всех узлов в его правом поддереве.

    Основано на DFS In-Order обходе.
    """
    st: list[Node[Any, Any]] = []
    prev_key = None

    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()

            if prev_key and node.key < prev_key:
                return False

            prev_key = node.key
            node = node.right

    return True


def is_general_bst(node: Node[Any, Any] | None) -> bool:
    """
    Проверка, является ли дерево общим BST. В общем BST каждый узел должен быть больше
    всех узлов его левого поддерева и меньше или равен всем узлам в его правом поддереве.

    Основано на DFS In-Order обходе.
    """
    st: list[Node[Any, Any]] = []
    prev = None

    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()

            # В общем дереве поиска ключи узлов могут быть равны, но тогда равный узел должен быть справа.
            if prev and (node.key < prev.key or node.key == prev.key and node.left is prev):
                return False

            prev = node
            node = node.right

    return True


def bst_visualize(node: Node[Any, Any] | None, level: int = 0) -> str:
    if node is None:
        return ""

    left = bst_visualize(node.left, level + 1)
    node_str = " " * 4 * level + "-> " + str(node.key) + "\n"
    right = bst_visualize(node.right, level + 1)

    return left + node_str + right


def update_attributes_recursive(node: Node[Any, Any]) -> None:
    for n in dfs(node, style="postorder", key=lambda _node: _node):
        n.update()
