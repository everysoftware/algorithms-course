from collections import deque
from collections.abc import Callable
from contextlib import suppress

INITIAL_CAPACITY = 8
P = 1_000_000_007
X = 263


class ChainingSet[T]:
    """Хеш-таблица с методом цепочек (закрытая адресация)."""

    def __init__(self, hash_function: Callable[[T], int], capacity: int = INITIAL_CAPACITY) -> None:
        self.hash_function = hash_function
        self.capacity = capacity
        # Основной массив цепочек: каждая ячейка — deque для O(1) вставки в начало
        self.table: list[deque[T]] = [deque() for _ in range(capacity)]

    def add(self, x: T) -> None:
        """Добавить элемент. Если уже есть — ничего не делать."""
        idx = self.hash_function(x) % self.capacity
        chain = self.table[idx]
        if x not in chain:
            chain.appendleft(x)  # добавление в начало цепочки

    def delete(self, x: T) -> None:
        """Удалить элемент. Если элемента нет — ничего не делать."""
        idx = self.hash_function(x) % self.capacity
        chain = self.table[idx]
        with suppress(ValueError):  # элемент не найден — молча выходим
            chain.remove(x)

    def find(self, x: T) -> bool:
        """Проверить наличие элемента."""
        idx = self.hash_function(x) % self.capacity
        return x in self.table[idx]

    def get_chain(self, i: int) -> str:
        """Вернуть содержимое i-й цепочки через пробел (как в условии)."""
        if 0 <= i < self.capacity:
            return " ".join(str(x) for x in self.table[i])
        return ""


def h(s: str) -> int:
    result = 0
    power = 1
    for ch in s:
        result = (result + ord(ch) * power) % P
        power = (power * X) % P
    return result


def chain_hashing(m: int, queries: list[tuple[str, str]]) -> list[str]:
    table = ChainingSet[str](h, m)
    output: list[str] = []

    for command, arg in queries:
        if command == "add":
            table.add(arg)
        elif command == "del":
            table.delete(arg)
        elif command == "find":
            output.append("yes" if table.find(arg) else "no")
        elif command == "check":
            idx = int(arg)
            output.append(table.get_chain(idx))
        else:
            raise NotImplementedError(f"Неизвестная команда: {command}")

    return output
