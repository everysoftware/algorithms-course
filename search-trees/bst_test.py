import random


class BSTTest:
    def __init__(self, tree):
        self.tree = tree
        self._update_keys()

    def _update_keys(self):
        if self.tree.root is None:
            self.keys = []
            self.size = 0
        else:
            self.keys = self.tree.in_order()
            self.size = len(self.keys)

    def test_print(self):
        print('TESTING PRINT')
        self.tree.self_print()

    def test_search(self):
        print('TESTING SEARCH')
        result = [self.tree.find(key) for key in self.keys]
        result.append(self.tree.find(float('inf')))
        result.append(self.tree.find(float('-inf')))
        print(*result, sep='\n')

    def test_addition(self, test_size=5):
        print('TESTING ADDITION')
        numbers = [random.randint(0, 20) for _ in range(test_size)]
        print(f'Generated numbers: {numbers}')
        for x in numbers:
            assert self.tree.add(x)
        assert self.tree.in_order() == sorted(self.keys + numbers)
        print('Result:')
        self.tree.self_print()
        self._update_keys()

    def test_max_min(self):
        print('TESTING MAX / MIN')
        print(f'Maximum: {self.tree.maximum()}')
        print(f'Minimum: {self.tree.minimum()}')

    def test_next(self):
        print('TESTING NEXT')
        result = []
        nxt = self.tree.minimum()
        while nxt is not None:
            curr = nxt
            result.append(curr.key)
            nxt = curr.next_element()
        print(f'Result: {result}')
        assert result == self.tree.in_order()

    def test_prev(self):
        print('TESTING PREV')
        result = []
        nxt = self.tree.maximum()
        while nxt is not None:
            curr = nxt
            result.append(curr.key)
            nxt = curr.prev_element()
        print(f'Result: {result}')
        assert result == self.tree.in_order()[::-1]

    def test_split_merge(self):
        print('TESTING SPLIT / MERGE')
        print('Root:')
        print(self.tree.root)
        print('Splitting the tree...')
        key = self.tree.root.key
        node1, node2 = self.tree.split(key)
        print('Left tree (new tree):')
        print(node1)
        node1.self_print()
        assert node1.in_order() == [x for x in self.keys if x <= key]
        print('Right tree:')
        print(node2)
        node2.self_print()
        assert node2.in_order() == [x for x in self.keys if x > key]
        print('Merging the trees...')
        self.tree.merge(node2)
        print('Merged (new tree):')
        print(self.tree.root)
        self.tree.self_print()
        assert self.tree.in_order() == self.keys

    def test_removal(self):
        print('TESTING REMOVAL')
        print(f'Keys: {self.keys}')
        k = self.size
        for key in self.keys:
            print(f'Delete {key}')
            assert self.tree.delete(key)
            self.tree.self_print()
            k -= 1
            assert k == len(self.tree.in_order())
        self._update_keys()

    def _test_all(self):
        tests = [self.test_print, self.test_search, self.test_addition,
                 self.test_max_min, self.test_next, self.test_prev,
                 self.test_split_merge, self.test_removal]
        for f in tests:
            f()
            print()

    def test_all(self):
        print('START FULL TESTING')
        self._test_all()
        print('FINISH FULL TESTING')
