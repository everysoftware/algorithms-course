from dataclasses import dataclass
from enum import Enum, auto

# -------------------------
# SLOT MODEL
# -------------------------


class SlotStatus(Enum):
    EMPTY = auto()
    ACTIVE = auto()
    DELETED = auto()


@dataclass
class Slot:
    status: SlotStatus = SlotStatus.EMPTY
    key: str | None = None
    value: int | None = None

    def set(self, key: str, value: int) -> None:
        self.status = SlotStatus.ACTIVE
        self.key = key
        self.value = value

    def delete(self) -> None:
        self.status = SlotStatus.DELETED
        self.key = None
        self.value = None


# -------------------------
# RESULT MODEL
# -------------------------


@dataclass
class OperationResult:
    key: str
    hash: int
    operation: str
    result: str
    value: str | None = None
    probing_index: int | None = None

    def __str__(self) -> str:
        parts = [
            f"key={self.key}",
            f"hash={self.hash}",
            f"operation={self.operation}",
            f"result={self.result}",
        ]

        if self.probing_index is not None:
            parts.append(f"linear_probing={self.probing_index}")

        if self.value is not None:
            parts.append(f"value={self.value}")

        return " ".join(parts)


# -------------------------
# HASH TABLE
# -------------------------


class HashTable:
    def __init__(self, q: int, p: int) -> None:
        self.capacity = q
        self.p = p
        self.table: list[Slot] = [Slot() for _ in range(q)]

    # -------------------------
    # PUT
    # -------------------------
    def put(self, key: str, value: int) -> OperationResult:
        h = self._hash(key)
        found, idx, collision = self._find_for_put(key)

        if found is not None:
            self.table[found].set(key, value)
            return OperationResult(key, h, "PUT", "inserted", str(value))

        if idx is not None and self.table[idx].status in (SlotStatus.EMPTY, SlotStatus.DELETED):
            self.table[idx].set(key, value)
            if not collision:
                return OperationResult(key, h, "PUT", "inserted", str(value))
            return OperationResult(key, h, "PUT", "collision", str(value), idx)

        return OperationResult(key, h, "PUT", "overflow")

    def get(self, key: str) -> OperationResult:
        h = self._hash(key)
        found, idx, collision = self._find_for_get(key)

        if found is not None:
            value = self.table[found].value
            if not collision:
                return OperationResult(key, h, "GET", "found", str(value))
            return OperationResult(key, h, "GET", "collision", str(value), found)

        if not collision:
            return OperationResult(key, h, "GET", "no_key")
        return OperationResult(key, h, "GET", "collision", "no_key", idx)

    def delete(self, key: str) -> OperationResult:
        h = self._hash(key)
        found, idx, collision = self._find_for_get(key)

        if found is not None:
            self.table[found].delete()
            if not collision:
                return OperationResult(key, h, "DEL", "removed")
            return OperationResult(key, h, "DEL", "collision", "removed", found)

        if not collision:
            return OperationResult(key, h, "DEL", "no_key")
        return OperationResult(key, h, "DEL", "collision", "no_key", idx)

    # -------------------------
    # HASH FUNCTION
    # -------------------------

    def _hash(self, key: str) -> int:
        result = 0
        for i, ch in enumerate(key):
            result = (result + (ord(ch) - ord("a") + 1) * pow(self.p, i, self.capacity)) % self.capacity
        return result

    # -------------------------
    # PROBING
    # -------------------------

    def _find_for_put(self, key: str) -> tuple[int | None, int, bool]:
        """Поиск слота для вставки: останавливается на EMPTY или DELETED."""
        start = self._hash(key)
        index = start
        collision = False

        for _ in range(self.capacity):
            slot = self.table[index]
            if slot.status in (SlotStatus.EMPTY, SlotStatus.DELETED):
                # Свободный слот для вставки.
                # Коллизия — только если мы уже прошли мимо ACTIVE с чужим ключом.
                return None, index, collision
            if slot.status == SlotStatus.ACTIVE:
                if slot.key == key:
                    return index, index, collision  # обновление существующего
                collision = True
            index = (index + 1) % self.capacity

        return None, index, True  # overflow

    def _find_for_get(self, key: str) -> tuple[int | None, int, bool]:
        """Поиск ключа: останавливается на EMPTY, игнорирует DELETED."""
        start = self._hash(key)
        index = start
        collision = False

        for _ in range(self.capacity):
            slot = self.table[index]
            if slot.status == SlotStatus.EMPTY:
                return None, index, collision
            if slot.status == SlotStatus.ACTIVE and slot.key == key:
                return index, index, collision
            if slot.status == SlotStatus.DELETED or (slot.status == SlotStatus.ACTIVE and slot.key != key):
                collision = True
            index = (index + 1) % self.capacity

        return None, index, True
