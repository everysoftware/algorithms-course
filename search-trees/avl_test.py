from bst_test import BSTTest
from avl_node import check_balance, check_height, check_size
from avl_tree import AVLTree


class AVLTest(BSTTest):
    def __init__(self, tree):
        if not isinstance(tree, AVLTree):
            raise ValueError
        super().__init__(tree)

    def check_tree_correctness(self, root=None):
        if root is None:
            root = self.tree.root
        super().check_tree_correctness(root)
        assert check_height(root)
        assert check_size(root)
        assert check_balance(root)

    def test_order_statistics(self):
        print('TESTING ORDER STATISTICS')
        result = [self.tree.order_statistics(k).key for k in range(1, self.size + 1)]
        print(f'Result: {result}')
        assert result == [x.key for x in self.tree.in_order()]

    def _test_all(self):
        tests = [self.test_print, self.test_search, self.test_insert,
                 self.test_max_min, self.test_order_statistics, self.test_next,
                 self.test_prev, self.test_split_merge, self.test_removal]
        for f in tests:
            f()
            self.check_tree_correctness()
            print()
