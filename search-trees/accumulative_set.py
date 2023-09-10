"""
Множество с запросами суммы на отрезке
"""

from avl_node import AVLNode, avl_merge, avl_split, check_height, check_size, check_balance
from avl_tree import AVLTree
from bst_node import print_d
from is_bst import is_bst


class SummingNode(AVLNode):
    def __init__(self, key=None, parent=None, left=None, right=None):
        super().__init__(key, parent, left, right)
        self.summa = key if key is not None else 0

    def __str__(self):
        left = self.left.key if self.left is not None else None
        right = self.right.key if self.right is not None else None
        parent = self.parent.key if self.parent is not None else None
        return f'SummingNode(K: {self.key}, SUM: {self.summa}, H: {self.height}, S: {self.size}, P: {parent}, ' \
               f'L: {left}, R: {right})'

    def update_attributes(self):
        super().update_attributes()
        update_summa(self)


def get_summa(node):
    return node.summa if node is not None else 0


def update_summa(node):
    node.summa = get_summa(node.left) + get_summa(node.right) + node.key


def check_summa_correctness(node):
    if node is None:
        return True
    return all(get_summa(x) == (get_summa(x.left) + get_summa(x.right) + x.key) for x in node.in_order())


def check_tree_correctness(root):
    assert is_bst(root)
    assert check_height(root)
    assert check_size(root)
    assert check_summa_correctness(root)
    assert check_balance(root)


class AccumulativeSet(AVLTree):
    node_type = SummingNode

    def __init__(self, root=None):
        super().__init__(root)

    def insert(self, key):
        result = self.find(key)
        if result is not None:
            return result
        return super().insert(key)

    def sum_between(self, left_num, right_num):
        left, temp = avl_split(self.root, left_num - 1)
        print('Left:')
        print_d(left)
        check_tree_correctness(left)
        print('Temp:')
        print_d(temp)
        check_tree_correctness(temp)
        middle, right = avl_split(temp, right_num)
        print('Middle:')
        print_d(middle)
        check_tree_correctness(middle)
        print('Right:')
        print_d(right)
        check_tree_correctness(right)
        res = get_summa(middle)
        temp = avl_merge(middle, right)
        print('Temp (Middle + Right):')
        print_d(temp)
        check_tree_correctness(temp)
        self.root = avl_merge(left, temp)
        check_tree_correctness(self.root)
        return res


def accumulative_set(queries):
    st = AccumulativeSet()
    s = 0

    def f(x):
        return (x + s) % 1_000_000_001

    result = []

    for i, args in enumerate(queries):
        option = args[0]
        print(f'Query #{i + 1}:', *args)
        if option == '?':
            key = f(int(args[1]))
            result.append((i + 1, 'Found' if st.key_exists(key) else 'Not found'))
        elif option == '+':
            key = f(int(args[1]))
            st.insert(key)
        elif option == 's':
            left, right = f(int(args[1])), f(int(args[2]))
            s = st.sum_between(left, right)
            result.append((i + 1, s))
        elif option == '-':
            key = f(int(args[1]))
            st.delete(key)

        check_tree_correctness(st.root)

        print('Tree after query:')
        st.print()
        print()
        print()

    return result
