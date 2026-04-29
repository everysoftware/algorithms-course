import pytest

from src.hash_tables.open_address import (
    OpenAddressHashMap,
)

# ---------------------------------------------------------------------------
# Вспомогательные хэш-функции
# ---------------------------------------------------------------------------


def constant_hash(x) -> int:
    """Все ключи попадают в одно и то же место — крайняя коллизия."""
    return 0


def identity_hash(x: int) -> int:
    """Для целочисленных ключей — сам ключ."""
    return x


def negative_hash(x: int) -> int:
    """Хэш, возвращающий отрицательные числа (проверка модуля)."""
    return -abs(x)


# ---------------------------------------------------------------------------
# Тесты базовых операций
# ---------------------------------------------------------------------------


class TestBasicOperations:
    def test_add_and_get_single(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        m.add(10, "a")
        assert m.get(10) == "a"

    def test_get_missing_returns_none(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        assert m.get(1) is None

    def test_get_missing_with_default(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        assert m.get(1, "default") == "default"
        # default может быть любым объектом, в том числе None
        assert m.get(1, None) is None
        # ключ существует — default игнорируется
        m.add(1, "value")
        assert m.get(1, "default") == "value"

    def test_add_updates_existing(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        m.add(5, "first")
        m.add(5, "second")
        assert m.get(5) == "second"
        # размер не должен увеличиться при обновлении
        assert m.size == 1

    def test_delete_existing(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        m.add(7, "x")
        m.delete(7)
        assert m.get(7) is None
        assert m.size == 0

    def test_delete_raises_keyerror_for_missing(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        with pytest.raises(KeyError):
            m.delete(99)

    def test_delete_twice_raises_keyerror(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        m.add(3, "v")
        m.delete(3)
        with pytest.raises(KeyError):
            m.delete(3)  # уже DELETED, не ACTIVE

    def test_size_after_operations(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash)
        assert m.size == 0
        m.add(1, "a")
        assert m.size == 1
        m.add(2, "b")
        assert m.size == 2
        m.add(2, "b2")  # обновление
        assert m.size == 2
        m.delete(1)
        assert m.size == 1
        m.delete(2)
        assert m.size == 0


# ---------------------------------------------------------------------------
# Тесты коллизий и линейного пробирования
# ---------------------------------------------------------------------------


class TestCollisionsAndProbing:
    def test_linear_probing_insert(self) -> None:
        # Все ключи получают индекс 0, заполняем подряд
        m = OpenAddressHashMap[int, str](constant_hash, capacity=8)
        keys = [10, 20, 30, 40, 50]
        for k in keys:
            m.add(k, str(k))
        # Должны занять слоты 0..4
        for k in keys:
            assert m.get(k) == str(k)
        # Проверим состояние таблицы
        assert m.table[0].key == 10
        assert m.table[1].key == 20
        assert m.table[2].key == 30
        assert m.table[3].key == 40
        assert m.table[4].key == 50
        assert m.table[5].is_empty()

    def test_tombstone_usage(self) -> None:
        m = OpenAddressHashMap[int, str](constant_hash, capacity=8)
        m.add(1, "one")
        m.add(2, "two")
        m.add(3, "three")
        m.add(4, "four")
        m.add(5, "five")  # слоты 0..4 заняты
        m.delete(2)  # слот 1 становится DELETED
        m.delete(4)  # слот 3 становится DELETED

        # Вставляем новый ключ — должен занять первый tombstone (индекс 1)
        m.add(6, "six")
        assert m.table[1].key == 6
        assert m.table[1].value == "six"
        assert m.table[1].is_active()
        # Старый ключ 2 не должен находиться
        assert m.get(2) is None
        assert m.get(4) is None
        # Ключи 1,3,4,5 всё ещё на месте
        assert m.get(1) == "one"
        assert m.get(3) == "three"
        assert m.get(5) == "five"
        assert m.get(6) == "six"

    def test_search_stops_at_empty(self) -> None:
        """Поиск несуществующего ключа останавливается на EMPTY,
        даже если дальше есть DELETED и ACTIVE."""
        m = OpenAddressHashMap[int, str](constant_hash, capacity=8)
        m.add(10, "a")
        m.add(20, "b")  # слот 1
        m.delete(10)  # слот 0 -> DELETED
        # Теперь слоты: 0 DELETED, 1 ACTIVE(20), 2..7 EMPTY
        # Ищем ключ 99 (нет в таблице). Пробирование идёт с 0:
        # 0 DELETED -> пропускаем; 1 ACTIVE но ключ 20 != 99;
        # 2 EMPTY -> возвращаем None.
        assert m.get(99) is None

    def test_probe_wraps_around(self) -> None:
        """Проверка закольцовывания probing."""
        m = OpenAddressHashMap[int, str](identity_hash, capacity=8)
        # Займём слоты 7, 0, 1
        m.add(7, "a")
        m.add(8, "b")  # 8 % 8 = 0 -> попадёт в 0
        m.add(9, "c")  # 9 % 8 = 1 -> попадёт в 1
        # Теперь добавляем ключ 15 (15 % 8 = 7). Он должен попасть в 2 после пробирования.
        m.add(15, "d")
        assert m.table[2].key == 15
        assert m.table[2].value == "d"


# ---------------------------------------------------------------------------
# Тесты рехеширования
# ---------------------------------------------------------------------------


class TestRehash:
    def test_rehash_triggers_on_load_factor(self) -> None:
        # capacity=8, 6 элементов -> 0.75, следующий add вызовет rehash
        m = OpenAddressHashMap[int, str](identity_hash, capacity=8)
        for i in range(6):
            m.add(i, str(i))
        assert m.capacity == 8
        assert m.size == 6

        # Добавляем 7-й элемент — должен сработать rehash
        m.add(6, "6")
        assert m.capacity == 16  # 8 * GROWTH_FACTOR
        # Все 7 ключей должны быть доступны
        for i in range(7):
            assert m.get(i) == str(i)

    def test_rehash_preserves_data(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash, capacity=4)  # начнём с маленькой capacity
        elements = [(1, "a"), (2, "b"), (3, "c")]
        for k, v in elements:
            m.add(k, v)
        # 3/4 = 0.75, порог достигнут, добавим четвёртый — должен произойти rehash
        m.add(4, "d")
        assert m.capacity == 8
        for k, v in [*elements, (4, "d")]:
            assert m.get(k) == v
        # Размер корректен
        assert m.size == 4

    def test_rehash_with_tombstones(self) -> None:
        """Rehash не переносит DELETED слоты."""
        m = OpenAddressHashMap[int, str](identity_hash, capacity=8)
        for i in range(6):
            m.add(i, str(i))
        # Удалим два элемента
        m.delete(1)
        m.delete(3)
        assert m.size == 4
        # Добавим новый, который вызовет rehash (size=5 при вставке? 4 + 1 = 5,
        # 5/8=0.625 < 0.75, rehash не будет. Чтобы вызвать rehash, нужно добавить
        # больше. Добавим ещё 2 ключа: сейчас size=4, добавим 6 и 7 -> size=6,
        # 6/8=0.75, затем добавим 8 -> rehash.
        m.add(6, "six")
        m.add(7, "seven")
        assert m.size == 6
        m.add(8, "eight")  # триггерит rehash
        assert m.capacity == 16
        # Проверяем наличие всех активных ключей
        active_keys = [0, 2, 4, 5, 6, 7, 8]
        for k in active_keys:
            assert m.get(k) is not None
        # Удалённые ключи отсутствуют
        assert m.get(1) is None
        assert m.get(3) is None


# ---------------------------------------------------------------------------
# Тесты поведения с пустой таблицей, только с DELETED, без EMPTY
# ---------------------------------------------------------------------------


class TestEdgeCasesWithStatuses:
    def test_all_slots_deleted_search(self) -> None:
        """Если все слоты DELETED, поиск возвращает None."""
        m = OpenAddressHashMap[int, str](constant_hash, capacity=4)
        m.add(1, "a")
        m.add(2, "b")
        m.add(3, "c")
        m.add(4, "d")  # все 4 слота заняты
        for k in (1, 2, 3, 4):
            m.delete(k)
        # Теперь все слоты DELETED, size=0
        assert m.size == 0
        # Поиск любого ключа проходит через все слоты и возвращает None
        assert m.get(1) is None
        assert m.get(99) is None

    def test_insert_into_all_deleted_table(self) -> None:
        """Вставка в таблицу, где все слоты DELETED, использует tombstone."""
        m = OpenAddressHashMap[int, str](constant_hash, capacity=4)
        for k in range(4):
            m.add(k, str(k))
        for k in range(4):
            m.delete(k)
        # Вставляем новый ключ, size=0 -> фактор 0, rehash не будет
        m.add(100, "new")
        assert m.size == 1
        # Ключ должен быть доступен
        assert m.get(100) == "new"
        # Первый же tombstone (индекс 0) стал ACTIVE
        assert m.table[0].key == 100
        assert m.table[0].is_active()

    def test_mixed_deleted_and_empty(self) -> None:
        """Проверка, что вставка предпочитает первый tombstone, а не EMPTY."""
        m = OpenAddressHashMap[int, str](constant_hash, capacity=4)
        m.add(10, "a")
        m.add(20, "b")  # слот 1
        m.delete(10)  # слот 0 -> DELETED
        # Теперь: 0 DELETED, 1 ACTIVE(20), 2 EMPTY, 3 EMPTY
        m.add(30, "c")  # должен занять слот 0, а не 2
        assert m.table[0].key == 30
        assert m.table[0].value == "c"
        assert m.table[2].is_empty()


# ---------------------------------------------------------------------------
# Тесты на граничные ключи и хэш-функции
# ---------------------------------------------------------------------------


class TestSpecialKeysAndHashes:
    def test_negative_hash_index(self) -> None:
        """Хэш возвращает отрицательное число — модуль должен дать
        корректный положительный индекс."""
        m = OpenAddressHashMap[int, str](negative_hash, capacity=8)
        m.add(3, "value")  # hash = -3, -3 % 8 = 5
        # Проверяем, что ключ доступен
        assert m.get(3) == "value"

    def test_none_key(self) -> None:
        """Ключ None допустим, если hash_function поддерживает None."""
        m = OpenAddressHashMap[None, str](hash, capacity=8)  # встроенный hash умеет None
        m.add(None, "none_value")
        assert m.get(None) == "none_value"
        m.delete(None)
        assert m.get(None) is None

    def test_none_value(self) -> None:
        """Значения могут быть None."""
        m = OpenAddressHashMap[int, str | None](identity_hash)
        m.add(1, None)
        assert m.get(1) is None
        # Проверяем, что ключ существует (get с default, который не None)
        assert m.get(1, "missing") is None  # вернёт None, а не "missing"
        # Убедимся, что ключ именно присутствует, а не отсутствует
        m.add(2, "check")
        assert m.get(1, "missing") is None

    def test_string_keys(self) -> None:
        m = OpenAddressHashMap[str, str](hash, capacity=8)
        m.add("hello", "world")
        assert m.get("hello") == "world"
        m.add("hello", "updated")
        assert m.get("hello") == "updated"

    def test_float_keys(self) -> None:
        m = OpenAddressHashMap[float, str](hash)
        m.add(3.14, "pi")
        assert m.get(3.14) == "pi"


# ---------------------------------------------------------------------------
# Дополнительные тесты на внутренние механики (проверка статусов)
# ---------------------------------------------------------------------------


class TestSlotStatusIntegrity:
    def test_slot_empties_after_delete(self) -> None:
        m = OpenAddressHashMap[int, str](identity_hash, capacity=4)
        m.add(1, "a")
        m.delete(1)
        slot = m.table[1 % 4]  # индекс зависит от хэша
        assert slot.is_deleted()
        assert not slot.is_active()
        assert slot.key is None
        assert slot.value is None

    def test_no_active_slots_after_clear_all(self) -> None:
        m = OpenAddressHashMap[int, int](identity_hash, capacity=4)
        keys = [0, 4, 8, 12]  # займут 0,1,2,3
        for k in keys:
            m.add(k, k)
        for k in keys:
            m.delete(k)
        for slot in m.table:
            assert not slot.is_active()
        assert m.size == 0
