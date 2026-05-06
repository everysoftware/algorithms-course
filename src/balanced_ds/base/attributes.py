from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Generic, TypeVar, cast

if TYPE_CHECKING:
    from src.balanced_ds.base.node import Node

T = TypeVar("T")


@dataclass
class Attribute(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def value(cls, node: Node[Any, Any] | None) -> T:
        pass

    @classmethod
    @abstractmethod
    def updated(cls, node: Node[Any, Any]) -> T:
        pass

    @classmethod
    @abstractmethod
    def update(cls, node: Node[Any, Any] | None) -> None:
        pass

    @classmethod
    def check(cls, node: Node[Any, Any] | None) -> bool:
        return node is None or cls.value(node) == cls.updated(node)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}()"

    def __repr__(self) -> str:
        return str(self)


@dataclass
class Height(Attribute[int]):
    @classmethod
    def empty_value(cls) -> int:
        return 0

    @classmethod
    def value(cls, node: Node[Any, Any] | None) -> int:
        if node is None:
            return cls.empty_value()

        return node.height

    @classmethod
    def updated(cls, node: Node[Any, Any]) -> int:
        return 1 + max(cls.value(node.left), cls.value(node.right))

    @classmethod
    def update(cls, node: Node[Any, Any] | None) -> None:
        if node is None:
            return

        node.height = cls.updated(node)


@dataclass
class Size(Attribute[int]):
    @classmethod
    def empty_value(cls) -> int:
        return 0

    @classmethod
    def value(cls, node: Node[Any, Any] | None) -> int:
        if node is None:
            return cls.empty_value()

        return node.size

    @classmethod
    def updated(cls, node: Node[Any, Any]) -> int:
        return 1 + cls.value(node.left) + cls.value(node.right)

    @classmethod
    def update(cls, node: Node[Any, Any] | None) -> None:
        if node is None:
            return

        node.size = cls.updated(node)


@dataclass
class Summa(Attribute[T], ABC):
    @classmethod
    @abstractmethod
    def empty_value(cls) -> T:
        pass

    @classmethod
    def value(cls, node: Node[Any, Any] | None) -> T:
        if node is None:
            return cls.empty_value()

        return cast(T, node.summa)

    @classmethod
    def updated(cls, node: Node[Any, Any]) -> T:
        value = node.key + cls.value(node.left) + cls.value(node.right)
        return cast(T, value)

    @classmethod
    def update(cls, node: Node[Any, Any] | None) -> None:
        if node is None:
            return

        node.summa = cls.updated(node)


class IntSumma(Summa[int]):
    @classmethod
    def empty_value(cls) -> int:
        return 0
