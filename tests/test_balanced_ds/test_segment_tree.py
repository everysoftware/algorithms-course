import pytest

from src.balanced_ds.segment_tree import IntSegmentTree
from tests.test_balanced_ds.random_samples import get_random_segment_tree_samples


@pytest.mark.run(order=5)
class TestAVLSegmentTree:
    @pytest.mark.parametrize("st", get_random_segment_tree_samples())
    def test_sum_between(self, st: IntSegmentTree) -> None:
        keys = sorted(st.dfs())

        for i in range(len(keys)):
            for j in range(i, len(keys)):
                left = keys[i]
                right = keys[j]
                assert st.sum_between(left, right) == sum(keys[i : j + 1])
