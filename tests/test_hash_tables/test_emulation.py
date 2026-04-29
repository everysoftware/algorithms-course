from typing import Any

import pytest

from src.hash_tables.emulation import HashTable, OperationResult


def result_dict(res: OperationResult) -> dict[str, Any]:
    """Преобразует результат в словарь для удобного сравнения."""
    d = {
        "key": res.key,
        "hash": res.hash,
        "operation": res.operation,
        "result": res.result,
    }
    if res.value is not None:
        d["value"] = res.value
    if res.probing_index is not None:
        d["linear_probing"] = res.probing_index
    return d


# ------------------------------------------------------------------
# Хеш-функция
# ------------------------------------------------------------------
class TestHashFunction:
    def test_basic(self) -> None:
        ht = HashTable(q=10, p=3)
        assert ht._hash("a") == 1  # 1*1 mod 10

    def test_multiple_chars(self) -> None:
        ht = HashTable(q=7, p=5)
        # 'abc': (1 + 2*5 + 3*25) mod 7 = 86 mod 7 = 2
        assert ht._hash("abc") == 2

    def test_same_hash_different_strings(self) -> None:
        ht = HashTable(q=3, p=2)
        # 'a'=1, 'd'=4 → оба 1 mod 3 (при p=2: 1*1=1, 4*1=4 mod3=1)
        assert ht._hash("a") == ht._hash("d") == 1


# ------------------------------------------------------------------
# Базовые операции без коллизий
# ------------------------------------------------------------------
class TestNoCollisions:
    @pytest.fixture()
    def empty_table(self) -> HashTable:
        return HashTable(q=10, p=31)

    def test_put_inserted(self, empty_table: HashTable) -> None:
        res = empty_table.put("key1", 100)
        h = empty_table._hash("key1")
        assert result_dict(res) == {"key": "key1", "hash": h, "operation": "PUT", "result": "inserted", "value": "100"}

    def test_get_found(self, empty_table: HashTable) -> None:
        empty_table.put("key1", 200)
        res = empty_table.get("key1")
        h = empty_table._hash("key1")
        assert result_dict(res) == {"key": "key1", "hash": h, "operation": "GET", "result": "found", "value": "200"}

    def test_get_no_key(self, empty_table: HashTable) -> None:
        res = empty_table.get("missing")
        h = empty_table._hash("missing")
        assert result_dict(res) == {"key": "missing", "hash": h, "operation": "GET", "result": "no_key"}

    def test_delete_removed(self, empty_table: HashTable) -> None:
        empty_table.put("key1", 300)
        res = empty_table.delete("key1")
        h = empty_table._hash("key1")
        assert result_dict(res) == {"key": "key1", "hash": h, "operation": "DEL", "result": "removed"}
        # После удаления слот DELETED, следующая ячейка EMPTY → это коллизия
        get_res = empty_table.get("key1")
        assert get_res.result == "collision"
        # probing_index — следующая EMPTY-ячейка после хеша
        # (hash + 1) % q, если нет других ключей
        assert get_res.probing_index == (h + 1) % 10
        assert get_res.value == "no_key"

    def test_delete_no_key(self, empty_table: HashTable) -> None:
        res = empty_table.delete("ghost")
        h = empty_table._hash("ghost")
        assert result_dict(res) == {"key": "ghost", "hash": h, "operation": "DEL", "result": "no_key"}


# ------------------------------------------------------------------
# Операции с коллизиями
# ------------------------------------------------------------------
class TestCollisions:
    @pytest.fixture()
    def small_table(self) -> HashTable:
        """Таблица размером 3, p=1 (хеш = код первого символа % 3)."""
        return HashTable(q=3, p=1)

    def test_put_collision(self, small_table: HashTable) -> None:
        # 'a'=1 -> hash=1, ячейка 1
        small_table.put("a", 10)
        # 'd'=4%3=1 -> коллизия, probing остановится на 2
        res = small_table.put("d", 20)
        assert result_dict(res) == {
            "key": "d",
            "hash": 1,
            "operation": "PUT",
            "result": "collision",
            "linear_probing": 2,
            "value": "20",
        }

    def test_get_collision_found(self, small_table: HashTable) -> None:
        small_table.put("a", 10)  # hash=1 → ячейка 1
        small_table.put("d", 20)  # hash=1 → коллизия, ячейка 2
        res = small_table.get("d")
        assert result_dict(res) == {
            "key": "d",
            "hash": 1,
            "operation": "GET",
            "result": "collision",
            "linear_probing": 2,
            "value": "20",
        }

    def test_get_collision_no_key(self, small_table: HashTable) -> None:
        small_table.put("a", 10)  # ячейка 1 занята
        # 'd'=1 (коллизия), следующая ячейка 2 EMPTY → останов
        res = small_table.get("d")
        assert result_dict(res) == {
            "key": "d",
            "hash": 1,
            "operation": "GET",
            "result": "collision",
            "linear_probing": 2,
            "value": "no_key",
        }

    def test_delete_collision_removed(self, small_table: HashTable) -> None:
        small_table.put("a", 10)  # ячейка 1
        small_table.put("d", 20)  # ячейка 2 (коллизия)
        res = small_table.delete("d")
        assert result_dict(res) == {
            "key": "d",
            "hash": 1,
            "operation": "DEL",
            "result": "collision",
            "linear_probing": 2,
            "value": "removed",
        }
        # после удаления 'd' ячейка 2 DELETED, дальнейший поиск 'd':
        # старт 1 (ACTIVE 'a'), 2 (DELETED), 0 (EMPTY) → стоп
        get_res = small_table.get("d")
        assert result_dict(get_res) == {
            "key": "d",
            "hash": 1,
            "operation": "GET",
            "result": "collision",
            "linear_probing": 0,
            "value": "no_key",
        }

    def test_delete_collision_no_key(self, small_table: HashTable) -> None:
        small_table.put("a", 10)  # ячейка 1 занята
        # 'd'=1 -> коллизия, следующая 2 EMPTY → останов
        res = small_table.delete("d")
        assert result_dict(res) == {
            "key": "d",
            "hash": 1,
            "operation": "DEL",
            "result": "collision",
            "linear_probing": 2,
            "value": "no_key",
        }


# ------------------------------------------------------------------
# Переполнение (overflow)
# ------------------------------------------------------------------
class TestOverflow:
    def test_put_overflow(self) -> None:
        ht = HashTable(q=2, p=1)
        ht.put("a", 1)  # hash=1 → ячейка 1
        ht.put("b", 2)  # 'b'=2%2=0 → ячейка 0
        # таблица полностью ACTIVE
        res = ht.put("c", 3)  # 'c'=3%2=1 → весь probing занят
        assert result_dict(res) == {"key": "c", "hash": 1, "operation": "PUT", "result": "overflow"}

    def test_put_on_deleted_slot(self) -> None:
        ht = HashTable(q=2, p=1)
        ht.put("a", 1)  # ячейка 1
        ht.put("b", 2)  # ячейка 0
        ht.delete("a")  # ячейка 1 DELETED
        # Вставляем ключ с хешем 1 — попадаем в DELETED, без коллизий
        res = ht.put("c", 3)  # 'c' = 3 % 2 = 1
        assert result_dict(res) == {"key": "c", "hash": 1, "operation": "PUT", "result": "inserted", "value": "3"}


# ------------------------------------------------------------------
# Поведение tombstone (DELETED)
# ------------------------------------------------------------------
class TestTombstoneBehavior:
    def test_probe_skips_deleted(self) -> None:
        """Поиск игнорирует DELETED и идёт до EMPTY."""
        ht = HashTable(q=4, p=1)
        ht.put("a", 1)  # 'a'=1 → ячейка 1
        ht.put("b", 2)  # 'b'=2 → ячейка 2
        ht.delete("a")  # ячейка 1 DELETED
        # ищем 'e' (5%4=1): старт 1 DELETED, 2 ACTIVE 'b', 3 EMPTY → стоп
        res = ht.get("e")
        assert result_dict(res) == {
            "key": "e",
            "hash": 1,
            "operation": "GET",
            "result": "collision",
            "linear_probing": 3,
            "value": "no_key",
        }

    def test_delete_already_deleted(self) -> None:
        """Повторное удаление уже удалённого ключа — no_key с коллизией."""
        ht = HashTable(q=3, p=1)
        ht.put("a", 1)  # ячейка 1
        ht.delete("a")  # → removed
        # повторное удаление: старт 1 DELETED, 2 EMPTY → стоп
        res = ht.delete("a")
        assert result_dict(res) == {
            "key": "a",
            "hash": 1,
            "operation": "DEL",
            "result": "collision",
            "linear_probing": 2,
            "value": "no_key",
        }


# ------------------------------------------------------------------
# Перезапись существующего ключа (UPDATE)
# ------------------------------------------------------------------
class TestUpdate:
    def test_put_existing_key(self) -> None:
        ht = HashTable(q=10, p=31)
        ht.put("key", 42)
        res = ht.put("key", 99)
        h = ht._hash("key")
        assert result_dict(res) == {"key": "key", "hash": h, "operation": "PUT", "result": "inserted", "value": "99"}
        get_res = ht.get("key")
        assert get_res.value == "99"

    def test_put_existing_key_after_collision(self) -> None:
        ht = HashTable(q=2, p=1)
        ht.put("a", 1)  # hash=1 → ячейка 1
        ht.put("c", 2)  # 'c'=3%2=1 → коллизия, записалась в 0
        res = ht.put("c", 77)
        assert result_dict(res) == {"key": "c", "hash": 1, "operation": "PUT", "result": "inserted", "value": "77"}
        get_res = ht.get("c")
        assert get_res.value == "77"


# ------------------------------------------------------------------
# Формат вывода (str результата)
# ------------------------------------------------------------------
class TestOutputFormat:
    def test_str_method(self) -> None:
        res = OperationResult("mykey", 5, "PUT", "inserted", "10", None)
        expected = "key=mykey hash=5 operation=PUT result=inserted value=10"
        assert str(res) == expected

        res2 = OperationResult("k", 3, "GET", "collision", "no_key", 7)
        expected2 = "key=k hash=3 operation=GET result=collision linear_probing=7 value=no_key"
        assert str(res2) == expected2


class TestTaskScenario:
    def test_test_9(self) -> None:
        ht = HashTable(q=17, p=31)
        ht.put("jfkmfith", 123)
        ht.delete("jfkmfith")
        get_res = ht.get("jfkmfith")
        assert get_res.probing_index == 3
        assert get_res.result == "collision"
        put_res = ht.put("kc", 64)
        assert put_res.result == "inserted"
        assert put_res.hash == 2
        get_kc = ht.get("kc")
        assert get_kc.result == "found"
        assert get_kc.value == "64"
