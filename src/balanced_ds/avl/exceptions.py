from typing import Any

from src.balanced_ds.base.exceptions import TreeError
from src.balanced_ds.base.node import Node


class ImbalancedError(TreeError):
    def __init__(self, node: Node[Any, Any], balance: int) -> None:
        super().__init__(f"Balance condition violated at node: {node} with balance: {balance}")
