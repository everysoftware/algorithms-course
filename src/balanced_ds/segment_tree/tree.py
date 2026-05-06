from typing import ClassVar

from src.balanced_ds.avl.tree import AVLTree
from src.balanced_ds.segment_tree.node import IntSegmentTreeNode
from src.balanced_ds.segment_tree.utils import sum_between


class IntSegmentTree(AVLTree[int, bool]):
    node_type: ClassVar[type[IntSegmentTreeNode]] = IntSegmentTreeNode

    def sum_between(self, lo: int, hi: int) -> int:
        """Сумма на отрезке от lo до hi включительно."""
        return sum_between(self, lo, hi)
