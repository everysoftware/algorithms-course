import random

from bst import BST
from is_bst import is_bst


class BSTTest:
    def __init__(self, tree):
        if not isinstance(tree, BST):
            raise ValueError
        self.tree = tree
        self._update_keys()

    def _update_keys(self):
        if self.tree.root is None:
            self.keys = []
            self.size = 0
        else:
            self.keys = [x.key for x in self.tree.in_order()]
            self.size = len(self.keys)

    def check_tree_correctness(self, root=None):
        if root is None:
            root = self.tree.root
        assert is_bst(root)

    def test_print(self):
        print('TESTING PRINT')
        self.tree.print()

    def test_search(self):
        print('TESTING SEARCH')
        result = [self.tree.find(key) for key in self.keys]
        result.append(self.tree.find(float('inf')))
        result.append(self.tree.find(float('-inf')))
        print(*result, sep='\n')

    def test_insert(self):
        print('TESTING INSERTION')
        numbers = [random.randint(0, 25) for _ in range(15)]
        print(f'Generated numbers: {numbers}')
        for x in numbers:
            self.tree.insert(x)
            self.check_tree_correctness()
        assert [x.key for x in self.tree.in_order()] == sorted(set(self.keys + numbers))
        print('Result:')
        self.tree.print()
        self._update_keys()

    def test_max_min(self):
        print('TESTING MAX / MIN')
        mx = self.tree.maximum()
        print(f'Maximum: {mx}')
        assert mx.key == max(self.keys)
        mn = self.tree.minimum()
        assert mn.key == min(self.keys)
        print(f'Minimum: {mn}')

    def test_next(self):
        print('TESTING NEXT')
        result = []
        nxt = self.tree.minimum()
        while nxt is not None:
            curr = nxt
            result.append(curr.key)
            nxt = curr.next_element()
        print(f'Result: {result}')
        assert result == [x.key for x in self.tree.in_order()]

    def test_prev(self):
        print('TESTING PREV')
        result = []
        nxt = self.tree.maximum()
        while nxt is not None:
            curr = nxt
            result.append(curr.key)
            nxt = curr.prev_element()
        print(f'Result: {result}')
        assert result == [x.key for x in self.tree.in_order()][::-1]

    def test_split_merge(self):
        print('TESTING SPLIT / MERGE')
        not_visited = self.keys.copy()
        random.shuffle(not_visited)
        print('TREE:')
        self.tree.print_d()
        while not_visited:
            key = not_visited.pop()
            print(f'Splitting the tree by {key}...')
            key = self.tree.root.key
            left, right = self.tree.split(key)
            print('LEFT:')
            left.print_d()
            self.check_tree_correctness(left)
            assert [x.key for x in left.in_order()] == [x for x in self.keys if x <= key]
            print('RIGHT:')
            right.print_d()
            self.check_tree_correctness(right)
            assert [x.key for x in right.in_order()] == [x for x in self.keys if x > key]
            print('Merging the trees...')
            self.tree.root = left
            self.tree.merge(right)
            print('MERGED:')
            self.tree.print_d()
            self.check_tree_correctness()
            assert [x.key for x in self.tree.in_order()] == self.keys

    def test_removal(self):
        print('TESTING REMOVAL')
        print(f'Keys: {self.keys}')
        k = self.size
        while self.keys:
            key = random.choice(self.keys)
            print(f'Delete {key}')
            self.tree.delete(key)
            self.tree.print_d()
            self.check_tree_correctness()
            k -= 1
            assert k == len(self.tree.in_order())
            self._update_keys()

    def _test_all(self):
        tests = [self.test_print, self.test_search, self.test_insert,
                 self.test_max_min, self.test_next, self.test_prev,
                 self.test_split_merge, self.test_removal]
        for f in tests:
            f()
            self.check_tree_correctness()
            print()

    def test_all(self):
        print('START FULL TESTING')
        self._test_all()
        print('FINISH FULL TESTING')
