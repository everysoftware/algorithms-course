from __future__ import annotations

from dataclasses import dataclass

from src.balanced_ds.base.node import K, V
from src.balanced_ds.bst.node import BSTNode


@dataclass
class AVLNode(BSTNode[K, V]):
    def __hash__(self) -> int:
        return hash((self.key, id(self)))
