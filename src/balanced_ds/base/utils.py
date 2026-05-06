from typing import Any

from src.balanced_ds.base.node import K, Node


def get_node_key(node: Node[K, Any]) -> K:
    return node.key
