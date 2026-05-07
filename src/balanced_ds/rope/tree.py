from __future__ import annotations

from typing import ClassVar, Self

from src.balanced_ds.avl.tree import AVLTree
from src.balanced_ds.rope.node import RopeNode
from src.balanced_ds.rope.operations import rope_build, rope_move_substr, rope_to_string


class Rope(AVLTree[int, str]):
    node_type: ClassVar[type[RopeNode]] = RopeNode

    @classmethod
    def from_string(cls, s: str) -> Self:
        return cls(rope_build(s))

    def move_substr(self, i: int, j: int, k: int) -> Rope:
        """
        Вырезает подстроку s[i:j + 1] и вставляет её после k-го символа оставшейся строки.
        """
        self.root = rope_move_substr(self.root, i, j, k)
        return self

    def to_string(self) -> str:
        """
        Возвращает строку.
        """
        return rope_to_string(self.root)
