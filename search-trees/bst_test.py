import random


class BSTTest:
    def __init__(self, bst):
        self.root = bst
        self._update_keys()

    def _update_keys(self):
        self.keys = self.root.dfs()
        self.tree_size = len(self.keys)

    def print_test(self):
        print('PRINT TEST')
        self.root.print()

    def find_test(self):
        print('FIND TEST')
        result = [self.root.find(key) for key in self.keys]
        result.append(self.root.find(float('inf')))
        result.append(self.root.find(float('-inf')))
        print(*result, sep='\n')

    def add_test(self, test_size=5):
        print('ADD TEST')
        numbers = [random.randint(0, 20) for _ in range(test_size)]
        print(f'Generated numbers: {numbers}')
        for x in numbers:
            assert self.root.add(x)
            self.root = self.root.root()
        assert self.root.dfs() == sorted(self.keys + numbers)
        print('Result:')
        self.root.print()
        self._update_keys()

    def max_min_test(self):
        print('MAX / MIN TEST')
        print(f'Maximum: {self.root.maximum()}')
        print(f'Minimum: {self.root.minimum()}')

    def next_test(self):
        print('NEXT TEST')
        result = []
        nxt = self.root.minimum()
        while nxt is not None:
            curr = nxt
            result.append(curr.key)
            nxt = curr.next_element()
        print(f'Result: {result}')
        assert result == self.root.dfs()

    def prev_test(self):
        print('PREV TEST')
        result = []
        nxt = self.root.maximum()
        while nxt is not None:
            curr = nxt
            result.append(curr.key)
            nxt = curr.prev_element()
        print(f'Result: {result}')
        assert result == self.root.dfs()[::-1]

    def delete_test(self):
        print('DELETE TEST')
        print(f'Keys: {self.keys}')
        k = self.tree_size
        for key in self.keys:
            print(f'Delete {key}')
            result = self.root.delete(key)
            self.root = self.root.root()
            k -= 1
            print('Result:')
            if not result and self.root.is_leaf():
                self.root = None
                print('Empty tree')
            else:
                self.root.print()
                assert result
                assert k == len(self.root.dfs())
        self.keys = []
        self.tree_size = 0

    def test_all(self):
        print('START FULL TESTING')
        tests = [self.print_test, self.find_test, self.add_test,
                 self.max_min_test, self.next_test, self.prev_test,
                 self.delete_test]
        for f in tests:
            f()
            print()
        print('FINISH FULL TESTING')
