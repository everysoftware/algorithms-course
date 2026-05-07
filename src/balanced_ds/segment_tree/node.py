from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar

from src.balanced_ds.avl.node import AVLNode
from src.balanced_ds.base.attributes import IntSumma

if TYPE_CHECKING:
    from collections.abc import Sequence

    from src.balanced_ds.base.attributes import Attribute


@dataclass
class IntSegmentTreeNode(AVLNode[int, None]):
    attributes_to_update: ClassVar[Sequence[type[Attribute[Any]]]] = [*list(AVLNode.attributes_to_update), IntSumma]

    def __hash__(self) -> int:
        return hash((self.key, id(self)))
