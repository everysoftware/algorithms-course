from bst_test import BSTTest


class AVLTest(BSTTest):
    def __init__(self, tree):
        super().__init__(tree)

    def test_order_statistics(self):
        print('TESTING ORDER STATISTICS')
        result = [self.tree.order_statistics(k).key for k in range(1, self.size + 1)]
        print(f'Result: {result}')
        assert result == self.tree.in_order()

    def _test_all(self):
        tests = [self.test_print, self.test_search, self.test_addition,
                 self.test_max_min, self.test_order_statistics, self.test_next,
                 self.test_prev, self.test_split_merge, self.test_removal]
        for f in tests:
            f()
            print()
