import random

import pytest

from src.balanced_ds.bst.tree import BST
from tests.test_balanced_ds.random_samples import get_random_bst_samples


@pytest.mark.run(order=3)
class TestBSTAdvanced:
    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_order_statistics(self, bst: BST[int, None]) -> None:
        keys = sorted(bst.dfs())

        for i, key in enumerate(keys):
            node = bst.order_statistics(i + 1)
            assert node is not None
            assert node.key == key

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_split(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        key = random.choice(keys)

        left, right = bst.split(key)

        left.check_correctness()
        right.check_correctness()

        assert left.dfs() == sorted([k for k in keys if k <= key])
        assert right.dfs() == sorted([k for k in keys if k > key])

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_merge(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        key = random.choice(keys)
        left, right = bst.split(key)

        merged = BST.merge(left, right)

        merged.check_correctness()
        assert merged.dfs() == keys
