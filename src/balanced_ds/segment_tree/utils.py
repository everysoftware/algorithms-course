from __future__ import annotations

from typing import TYPE_CHECKING

from src.balanced_ds.base.attributes import IntSumma

if TYPE_CHECKING:
    from src.balanced_ds.segment_tree import IntSegmentTree


def sum_between(tree: IntSegmentTree, lo: int, hi: int) -> int:
    """Сумма на отрезке от lo до hi включительно."""
    left, temp = tree.split(lo - 1)
    middle, right = temp.split(hi)

    result = IntSumma.value(middle.root)

    temp = middle.merge(right)
    tree.root = left.merge(temp).root

    return result
