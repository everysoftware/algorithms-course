from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

from src.balanced_ds.base.attributes import Attribute, Height, Size
from src.balanced_ds.base.node import K, Node, V


@dataclass
class BSTNode(Node[K, V]):
    attributes_to_update: ClassVar[Sequence[type[Attribute[Any]]]] = [Size, Height]

    def __hash__(self) -> int:
        return hash((self.key, id(self)))
