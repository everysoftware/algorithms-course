from typing import Any

from src.balanced_ds.avl.operations import avl_merge_with_root, balance
from src.balanced_ds.base.attributes import Size
from src.balanced_ds.base.node import Node, NodeT
from src.balanced_ds.bst.operations import bst_delete_child, bst_max, bst_prev, clear_parent
from src.balanced_ds.rope.node import RopeNode

"""
Во адаптированных из AVL функциях используется неявный ключ.

Неявный ключ - это размер поддерева, корнем которого является узел. То есть, если узел имеет неявный ключ x, то
все символы, которые находятся в левом поддереве этого узла, имеют неявные ключи от 1 до x - 1, а все символы,
которые находятся в правом поддереве этого узла, имеют неявные ключи от x + 1 до x + размер_правого_поддерева.
"""


def rope_delete(node: NodeT | None, i: int) -> NodeT | None:
    """Удалить s[i]."""
    stack = []
    current = node

    while current is not None:
        left_size = Size.value(current.left)

        # left_size + 1 - неявный ключ текущего узла (индекс символа в строке).
        if left_size + 1 == i:
            if current.left is None or current.right is None:
                current = bst_delete_child(current)
            else:
                swap_node = bst_prev(current)
                assert swap_node is not None
                current.key = swap_node.key
                current.value = swap_node.value
                current.left = None
                current = swap_node
        elif left_size + 1 > i:
            stack.append(current)
            current = current.left
        else:
            stack.append(current)
            current = current.right
            i -= left_size + 1

    # Балансируем все узлы, которые были изменены.
    while stack:
        current = stack.pop()
        current = balance(current)

    return current


def rope_merge(left: NodeT | None, right: NodeT | None) -> NodeT | None:
    """Склеить две строки."""
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left

    new_root = bst_max(left)
    left = rope_delete(left, Size.value(left))
    clear_parent(new_root)

    return avl_merge_with_root(left, right, new_root)


def rope_split(node: NodeT | None, i: int) -> tuple[NodeT | None, NodeT | None]:
    """Разделить строку на две подстроки: s[:i], s[i:]."""
    if node is None:
        return None, None

    left_size = Size.value(node.left)

    if left_size + 1 > i:
        left, temp = rope_split(node.left, i)
        clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        temp, right = rope_split(node.right, i - (left_size + 1))
        clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)

    clear_parent(left, right)

    return left, right


def rope_build_helper(s: str, left: int, right: int) -> Node[Any, Any]:
    if left < right:
        m = (left + right) // 2
        left_part = rope_build_helper(s, left, m)
        right_part = rope_build_helper(s, m + 1, right)

        node = rope_merge(left_part, right_part)
        assert node is not None
        return node
    else:
        return RopeNode(left, s[left])


def rope_build(s: str) -> Node[Any, Any]:
    """Построение Rope из строки."""
    return rope_build_helper(s, 0, len(s) - 1)


"""
Перемещение подстроки s[i:j + 1] на позицию k оставшейся строки.

Функция аналогична следующей:

def move_substring(self, i, j, k):
    without_sub = self.s[:i] + self.s[j + 1:]
    before = without_sub[:k]
    sub = self.s[i:j + 1]
    after = without_sub[k:]
    self.s = before + sub + after
    return self.s

Но работает за O(log n), где n - размер строки.

"""


def rope_move_substr(node: NodeT | None, i: int, j: int, k: int) -> NodeT | None:
    """Перемещение подстроки s[i:j + 1] на позицию k оставшейся строки"""
    if node is None:
        return None

    # Разделяем строку на две части: до i-го символа и начиная с i-го символа
    left, temp = rope_split(node, i)

    # Разделяем temp на две части: до j-го символа включительно и после j-го символа
    # Поскольку temp начинается с i-го символа, то делаем j - i.
    # После этого добавляем 1, чтобы включить j-ый символ в срез.
    sub, right = rope_split(temp, j - i + 1)

    # Объединяем левую и правую части строки без подстроки
    without_sub = rope_merge(left, right)

    # Разделяем without_sub на две части: до k-го символа включительно (k начинается с 1) и после k-го символа
    before, after = rope_split(without_sub, k)

    # Объединяем sub и after
    sub_and_after = rope_merge(sub, after)

    # Объединяем before и new_right
    return rope_merge(before, sub_and_after)


def rope_to_string(root: NodeT | None) -> str:
    """Получить строку из Rope."""
    st: list[NodeT] = []
    result = ""
    node = root

    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            result += node.value if node.value is not None else ""
            node = node.right

    return result
