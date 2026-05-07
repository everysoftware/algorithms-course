from typing import Any, Literal

from src.balanced_ds.base.attributes import Attribute
from src.balanced_ds.base.exceptions import TreeError
from src.balanced_ds.base.node import Node


class EmptyTreeError(TreeError):
    def __init__(self) -> None:
        super().__init__("Tree is empty")


class EmptyNodeError(TreeError):
    def __init__(self) -> None:
        super().__init__("Node is empty")


class CycleError(TreeError):
    def __init__(self, node: Node[Any, Any]) -> None:
        super().__init__(f"Cycle detected at node: {node}")


class ParentError(TreeError):
    def __init__(self, child: Literal["left", "right"], node: Node[Any, Any]) -> None:
        super().__init__(f"Parent of {child} child is not equal to node at node: {node}")


class NodeAttributeError(TreeError):
    def __init__(self, attribute: type[Attribute[Any]], node: Node[Any, Any]) -> None:
        super().__init__(
            f"Invalid attribute: {attribute.__name__} = {attribute.value(node)} "
            f"(expected: {attribute.updated(node)}) at node: {node}"
        )


class TraverseStyleError(TreeError):
    def __init__(self) -> None:
        super().__init__("Invalid traverse style")
