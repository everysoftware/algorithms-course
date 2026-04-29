from collections.abc import Callable
from enum import StrEnum, auto
from typing import Generic, Literal, TypeVar, overload

K = TypeVar("K")
V = TypeVar("V")

REHASH_FACTOR = 0.75
INITIAL_CAPACITY = 8
GROWTH_FACTOR = 2


class SlotStatus(StrEnum):
    EMPTY = auto()
    """Никогда не использовался"""
    ACTIVE = auto()
    """Содержит пару key-value"""
    DELETED = auto()
    """Был удалён (tombstone)"""


class Slot(Generic[K, V]):
    """Ячейка хеш-таблицы."""

    def __init__(self) -> None:
        self.status = SlotStatus.EMPTY
        self.key: K | None = None
        self.value: V | None = None

    def is_active(self) -> bool:
        return self.status == SlotStatus.ACTIVE

    def is_empty(self) -> bool:
        return self.status == SlotStatus.EMPTY

    def is_deleted(self) -> bool:
        return self.status == SlotStatus.DELETED

    def set(self, key: K, value: V) -> None:
        self.status = SlotStatus.ACTIVE
        self.key = key
        self.value = value

    def delete(self) -> None:
        self.status = SlotStatus.DELETED
        self.key = None
        self.value = None


class OpenAddressHashMap(Generic[K, V]):
    """
    HashMap с открытой адресацией и линейным пробированием.
    """

    def __init__(self, hash_function: Callable[[K], int], capacity: int = INITIAL_CAPACITY) -> None:
        self.hash_function = hash_function
        self.capacity = capacity
        self.size = 0
        self.table: list[Slot[K, V]] = [Slot() for _ in range(capacity)]

    # -------------------------
    # PUBLIC API
    # -------------------------

    def add(self, key: K, value: V) -> None:
        """Вставка или обновление значения."""
        if self.size / self.capacity >= REHASH_FACTOR:
            self._rehash()

        index, found = self._probe_for_insert(key)

        if not found:
            self.size += 1

        self.table[index].set(key, value)

    @overload
    def get(self, key: K, default: Literal[None] = None) -> V | None: ...

    @overload
    def get(self, key: K, default: V) -> V: ...

    def get(self, key: K, default: V | None = None) -> V | None:
        """Получение значения по ключу."""
        index = self._probe_for_search(key)
        if index is None:
            return default
        return self.table[index].value

    def delete(self, key: K) -> None:
        """Удаление ключа (tombstone)."""
        index = self._probe_for_search(key)
        if index is None:
            raise KeyError(key)

        if self.table[index].is_active():
            self.table[index].delete()
            self.size -= 1

    # -------------------------
    # PROBING LOGIC
    # -------------------------

    def _base_index(self, key: K) -> int:
        """Начальный индекс."""
        return self.hash_function(key) % self.capacity

    def _probe_for_search(self, key: K) -> int | None:
        """
        Поиск существующего ключа.
        Возвращает индекс или None.
        """
        index = self._base_index(key)

        for _ in range(self.capacity):
            slot = self.table[index]

            if slot.is_empty():
                return None  # ключ точно не существует

            if slot.is_active() and slot.key == key:
                return index

            index = (index + 1) % self.capacity

        return None

    def _probe_for_insert(self, key: K) -> tuple[int, bool]:
        """
        Поиск позиции для вставки.
        Возвращает:
        - индекс
        - найден ли уже ключ (для update vs insert)
        """
        index = self._base_index(key)

        first_deleted: int | None = None

        for _ in range(self.capacity):
            slot = self.table[index]

            # ключ уже существует → обновление
            if slot.is_active() and slot.key == key:
                return index, True

            # запоминаем первый tombstone
            if slot.is_deleted() and first_deleted is None:
                first_deleted = index

            # пустая ячейка — можем вставить сюда
            if slot.is_empty():
                return (first_deleted if first_deleted is not None else index), False

            index = (index + 1) % self.capacity

        # таблица "закольцована"
        return (first_deleted if first_deleted is not None else index), False

    # -------------------------
    # REHASH
    # -------------------------

    def _rehash(self) -> None:
        """
        Увеличение таблицы и перераспределение элементов.
        """
        old_table = self.table

        self.capacity *= GROWTH_FACTOR
        self.table = [Slot() for _ in range(self.capacity)]
        self.size = 0

        for slot in old_table:
            if slot.is_active():
                # вставляем заново через add (уже в новой таблице)
                assert slot.key is not None
                assert slot.value is not None
                self.add(slot.key, slot.value)
