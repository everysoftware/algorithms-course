from __future__ import annotations

from typing import Any, ClassVar, Generic

from src.balanced_ds.base.node import K, Node, V


class BinaryTree(Generic[K, V]):
    node_type: ClassVar[type[Node[Any, Any]]] = Node[K, V]
    root: Node[K, V] | None = None

    def __init__(self, root: Node[K, V] | None = None) -> None:
        self.root = root
