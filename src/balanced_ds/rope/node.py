from __future__ import annotations

from dataclasses import dataclass

from src.balanced_ds.avl.node import AVLNode


@dataclass
class RopeNode(AVLNode[int, str]):
    def __hash__(self) -> int:
        return hash((self.key, id(self)))
