"""
Rope
"""

from avl_node import AVLNode, balance, get_size, avl_merge_with_root, prev_element
from bst_node import clear_parent
from avl_tree import AVLTree


class NaiveRope:
    def __init__(self, s):
        self.s = s

    def move_substring(self, i, j, k):
        without_sub = self.s[:i] + self.s[j + 1:]
        before = without_sub[:k]
        sub = self.s[i:j + 1]
        after = without_sub[k:]
        self.s = before + sub + after
        return self.s


# Наивное решение. Сложность алгоритма: O(QN).
def rope_naive(s, queries):
    r = NaiveRope(s)
    for i, j, k in queries:
        r.move_substring(i, j, k)
    return r.s


class RopeNode(AVLNode):
    def __init__(self, key=None, value=None, parent=None, left=None, right=None):
        super().__init__(key, value, parent, left, right)

    def delete(self, i):
        """
        Удаляет i-й символ строки.
        """
        return rope_delete(self, i)

    def merge(self, other):
        """
        Конкатенация строк.
        """
        return rope_merge(self, other)

    def split(self, i):
        """
        Разрезает строку по i-му символу.
        Возвращает две подстроки: s[:i], s[i + 1:].
        """
        return rope_split(self, i)

    def move_substring(self, i, j, k):
        """
        Вырезает подстроку s[i:j + 1] и вставляет её после k-го символа оставшейся строки.
        """
        return move_substring(self, i, j, k)

    def get_str(self):
        """
        Возвращает строковое представление дерева.
        """
        return get_str(self)


def move_substring(node, i, j, k):
    s_len = get_size(node)
    left, temp = rope_split(node, i)
    middle, right = rope_split(temp, j - i + 1)
    without_sub = rope_merge(left, right)
    if k >= s_len - (j - i + 1):
        k = float('inf')
    elif k <= 0:
        k = float('-inf')
    new_left, temp = rope_split(without_sub, k)
    new_right = rope_merge(middle, temp)
    return rope_merge(new_left, new_right)


def rope_delete(node, i):
    stack = []
    current = node
    while current is not None:
        left_size = get_size(current.left)
        if left_size + 1 == i:
            if current.left is None or current.right is None:
                child = current.right if current.left is None else current.left
                if child is not None:
                    child.parent = current.parent
                if current.parent is not None:
                    if current.parent.left is current:
                        current.parent.left = child
                    else:
                        current.parent.right = child
                current = child
            else:
                swap_node = prev_element(current)
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
    while stack:
        current = stack.pop()
        current = balance(current)
    return current


def rope_merge(left, right):
    if left is None and right is None:
        return None
    elif left is None:
        return right
    elif right is None:
        return left
    new_root = left.maximum()
    left = rope_delete(left, get_size(left))
    clear_parent(new_root)
    return avl_merge_with_root(left, right, new_root)


def rope_split(node, i):
    if node is None:
        return None, None
    left_size = get_size(node.left)
    if left_size + 1 > i:
        left, temp = rope_split(node.left, i)
        clear_parent(temp, node.right)
        right = avl_merge_with_root(temp, node.right, node)
    else:
        temp, right = rope_split(node.right, i - left_size - 1)
        clear_parent(node.left, temp)
        left = avl_merge_with_root(node.left, temp, node)
    clear_parent(left, right)
    return left, right


def get_str(root):
    st = []
    result = ''
    node = root
    while st or node is not None:
        if node is not None:
            st.append(node)
            node = node.left
        else:
            node = st.pop()
            result += node.value
            node = node.right
    return result


class Rope(AVLTree):
    node_type = RopeNode

    def __init__(self, s=''):
        super().__init__()
        self.s = s
        self.root = self._build_from_str()

    def _build_from_str(self, left=0, right=None):
        right = right if right is not None else (len(self.s) - 1)
        if left < right:
            m = (left + right) // 2
            left_part = self._build_from_str(left, m)
            right_part = self._build_from_str(m + 1, right)
            return rope_merge(left_part, right_part)
        else:
            return self.node_type(left, self.s[left])

    def get_str(self):
        return self.root.get_str()

    def move_substring(self, i, j, k):
        self.root = self.root.move_substring(i, j, k)
        return self.root


# Решение через АВЛ-дерево. Сложность: O(QlogN).
def rope(s, queries):
    tree = Rope(s)
    for i, j, k in queries:
        tree.move_substring(i, j, k)
    return tree.get_str()
