from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, ClassVar, Generic, Self, TypeVar

from src.balanced_ds.base.attributes import Attribute, Height, Size

if TYPE_CHECKING:
    from collections.abc import Sequence

K = TypeVar("K", int, float, str, bool)
V = TypeVar("V", int, float, str, bool, None)
NodeT = TypeVar("NodeT", bound="Node[Any, Any]")


@dataclass
class Node(Generic[K, V]):
    attributes_to_update: ClassVar[Sequence[type[Attribute[Any]]]] = [Size, Height]

    key: K
    value: V | None = None
    left: Self | None = None
    right: Self | None = None
    parent: Self | None = None
    size: int = 1
    height: int = 1
    summa: K = field(init=False)

    def update(self) -> None:
        for attr in self.attributes_to_update:
            attr.update(self)

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.key}, {self.value})"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.key, id(self)))

    def __post_init__(self) -> None:
        self.summa = self.key
