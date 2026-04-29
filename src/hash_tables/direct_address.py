from typing import cast, overload

_EMPTY = object()
"""Уникальный маркер \"ячейка пуста\""""


class DirectAddressMap[V]:
    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("max_key must be non-negative")
        self._data: list[V | object] = [_EMPTY] * size

    def add(self, key: int, value: V) -> None:
        """Сохраняет значение по ключу (перезаписывает, если уже существует)."""
        self._check_key(key)
        self._data[key] = value

    @overload
    def get(self, key: int, default: None = None) -> V | None: ...

    @overload
    def get(self, key: int, default: V) -> V: ...

    def get(self, key: int, default: V | None = None) -> V | None:
        """Возвращает значение по ключу, или default (None) если ключ отсутствует."""
        self._check_key(key)
        entry = self._data[key]
        if entry is _EMPTY:
            return default
        return cast(V, entry)  # гарантированно не _EMPTY

    def delete(self, key: int) -> None:
        """Удаляет ключ; если ключ отсутствует — KeyError."""
        self._check_key(key)
        if self._data[key] is _EMPTY:
            raise KeyError(key)
        self._data[key] = _EMPTY

    def _check_key(self, key: int) -> None:
        """Проверяет, что ключ в допустимом диапазоне."""
        if not (0 <= key < len(self._data)):
            raise KeyError(key)
