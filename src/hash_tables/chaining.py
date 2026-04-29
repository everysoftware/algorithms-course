from collections.abc import Callable
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")

INITIAL_CAPACITY = 8
REHASH_FACTOR = 0.75
GROWTH_FACTOR = 2


class Slot(Generic[K, V]):
    """Пара ключ-значение."""

    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value


class ChainingHashMap(Generic[K, V]):
    """
    HashMap с закрытой адресацией (chaining).
    Каждая ячейка — список (цепочка коллизий).
    """

    def __init__(self, hash_function: Callable[[K], int], capacity: int = INITIAL_CAPACITY) -> None:
        self.hash_function = hash_function
        self.capacity = capacity
        self.size = 0

        # массив бакетов (каждый бакет — список Entry)
        self.table: list[list[Slot[K, V]]] = [[] for _ in range(capacity)]

    # -------------------------
    # HASH UTIL
    # -------------------------

    def _index(self, key: K) -> int:
        """Вычисление индекса бакета."""
        return self.hash_function(key) % self.capacity

    # -------------------------
    # PUBLIC API
    # -------------------------

    def add(self, key: K, value: V) -> None:
        """Вставка или обновление значения."""
        if self.size / self.capacity >= REHASH_FACTOR:
            self._rehash()

        index = self._index(key)
        bucket = self.table[index]

        # проверяем, есть ли ключ уже
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        # если нет — добавляем новый
        bucket.append(Slot(key, value))
        self.size += 1

    def get(self, key: K, default: V | None = None) -> V | None:
        """Получение значения по ключу."""
        index = self._index(key)
        bucket = self.table[index]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        return default

    def delete(self, key: K) -> None:
        """Удаление ключа."""
        index = self._index(key)
        bucket = self.table[index]

        for i, entry in enumerate(bucket):
            if entry.key == key:
                bucket.pop(i)
                self.size -= 1
                return

        raise KeyError(key)

    # -------------------------
    # REHASH
    # -------------------------

    def _rehash(self) -> None:
        """
        Увеличение таблицы и перераспределение элементов.
        """
        old_table = self.table

        self.capacity *= GROWTH_FACTOR
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_table:
            for entry in bucket:
                self.add(entry.key, entry.value)
