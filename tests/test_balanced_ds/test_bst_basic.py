import random

import pytest

from src.balanced_ds.bst.tree import BST
from tests.test_balanced_ds.random_samples import get_random_bst_samples, keys_samples


@pytest.mark.run(order=2)
class TestBSTBasic:
    @pytest.mark.parametrize("keys", keys_samples)
    def test_insert(self, keys: list[int]) -> None:
        bst = BST[int, None]()

        for key in keys:
            bst.insert(key)
            bst.check_correctness()

        assert bst.dfs() == sorted(set(keys))

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_contains(self, bst: BST[int, None]) -> None:
        for key in bst.dfs():
            assert bst.contains(key)

        assert not bst.contains(-1)

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_find(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            node = bst.find(key)
            assert node is not None
            assert node.key == key

        assert bst.find(-1) is None

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_min(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        random.shuffle(keys)

        min_key = min(keys)
        min_node = bst.min()
        assert min_node is not None
        assert min_node.key == min_key

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_max(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        random.shuffle(keys)

        max_key = max(keys)
        max_node = bst.max()
        assert max_node is not None
        assert max_node.key == max_key

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_next(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            next_node = bst.next(key)
            if key == max(keys):
                assert next_node is None
            else:
                assert next_node is not None
                assert next_node.key == min(filter(lambda x: x > key, keys))

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_prev(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            prev_node = bst.prev(key)
            if key == min(keys):
                assert prev_node is None
            else:
                assert prev_node is not None
                assert prev_node.key == max(filter(lambda x: x < key, keys))

    @pytest.mark.parametrize("bst", get_random_bst_samples())
    def test_delete(self, bst: BST[int, None]) -> None:
        keys = bst.dfs()
        random.shuffle(keys)

        for key in keys:
            bst.delete(key)
            bst.check_correctness()

        assert bst.dfs() == []

    def test_empty(self) -> None:
        bst = BST[int, None]()
        assert bst.empty()

        bst.insert(1)
        assert not bst.empty()

        bst.delete(1)
        assert bst.empty()
