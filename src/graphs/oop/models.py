from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Generic, Self, TypeVar, cast

K = TypeVar("K")
NodeT = TypeVar("NodeT", bound="Node[Any]")
Weight = float
EdgeData = tuple[K, K, Weight]


@dataclass
class Node(Generic[K]):
    """
    Узел графа.
    """

    key: K
    """Значение узла."""
    edges: list[Edge] = field(default_factory=list)
    """Список рёбер, ведущих из узла."""
    parents: dict[Self, Edge] = field(default_factory=dict)
    """Список родителей."""

    def __hash__(self) -> int:
        return hash(self.key)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return cast(bool, self.key == other.key)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.key})"


@dataclass
class Edge:
    """
    Ребро графа.
    """

    adjacent: Node[Any]
    """Узел, на который ведёт ребро."""
    weight: Weight
    """Вес ребра."""


@dataclass
class PathNode:
    """
    Узел пути.
    """

    node: Node[Any]
    """Узел."""
    parent: Self | None
    """Родительский узел."""

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.node})"
