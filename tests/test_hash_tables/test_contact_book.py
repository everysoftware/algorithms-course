from collections.abc import Callable

import pytest

from src.hash_tables.contact_book import contact_book_direct_address, contact_book_open_address

MAX_NUMBER = 10_000_000
PRIME = 11
FUNC_T = Callable[[list[tuple[str, str, str]]], list[str]]


# Параметризуем обе реализации
@pytest.mark.parametrize("func", [contact_book_direct_address, contact_book_open_address])
class TestContactBook:
    # Пустой список запросов
    def test_empty(self, func: FUNC_T) -> None:
        assert func([]) == []

    # Базовый сценарий из условия
    def test_basic_scenario(self, func: FUNC_T) -> None:
        queries = [
            ("add", "911", "police"),
            ("add", "76213", "Mom"),
            ("add", "17239", "Bob"),
            ("find", "76213", ""),
            ("find", "910", ""),
            ("find", "911", ""),
            ("del", "910", ""),
            ("del", "911", ""),
            ("find", "911", ""),
            ("find", "76213", ""),
            ("add", "76213", "daddy"),
            ("find", "76213", ""),
        ]
        expected = [
            "Mom",
            "not found",
            "police",
            "not found",
            "Mom",
            "daddy",
        ]
        assert func(queries) == expected

    # Добавление и поиск нескольких номеров
    def test_add_and_find_multiple(self, func: FUNC_T) -> None:
        queries = [
            ("add", "1", "Alice"),
            ("add", "2", "Bob"),
            ("add", "3", "Charlie"),
            ("find", "1", ""),
            ("find", "2", ""),
            ("find", "3", ""),
            ("find", "4", ""),
        ]
        expected = ["Alice", "Bob", "Charlie", "not found"]
        assert func(queries) == expected

    # Замена имени при повторном добавлении
    def test_add_replaces_name(self, func: FUNC_T) -> None:
        queries = [
            ("add", "42", "Old"),
            ("add", "42", "New"),
            ("find", "42", ""),
        ]
        expected = ["New"]
        assert func(queries) == expected

    # Удаление существующего номера
    def test_delete_existing(self, func: FUNC_T) -> None:
        queries = [
            ("add", "100", "Test"),
            ("find", "100", ""),
            ("del", "100", ""),
            ("find", "100", ""),
        ]
        expected = ["Test", "not found"]
        assert func(queries) == expected

    # Удаление несуществующего номера не влияет на остальные записи
    def test_delete_nonexisting(self, func: FUNC_T) -> None:
        queries = [
            ("add", "55", "Keeper"),
            ("del", "999", ""),
            ("find", "55", ""),
            ("find", "999", ""),
        ]
        expected = ["Keeper", "not found"]
        assert func(queries) == expected

    # Двойное удаление одного номера
    def test_double_delete(self, func: FUNC_T) -> None:
        queries = [
            ("add", "5", "Five"),
            ("del", "5", ""),
            ("del", "5", ""),
            ("find", "5", ""),
        ]
        expected = ["not found"]
        assert func(queries) == expected

    # Работа с граничными номерами (0 и MAX_NUMBER-1)
    def test_boundary_numbers(self, func: FUNC_T) -> None:
        max_num = MAX_NUMBER - 1
        queries = [
            ("add", "0", "Zero"),
            ("add", str(max_num), "Max"),
            ("find", "0", ""),
            ("find", str(max_num), ""),
            ("find", "1", ""),
            ("del", "0", ""),
            ("del", str(max_num), ""),
            ("find", "0", ""),
            ("find", str(max_num), ""),
        ]
        expected = [
            "Zero",
            "Max",
            "not found",
            "not found",
            "not found",
        ]
        assert func(queries) == expected

    # Смешанные операции: чередование add/del/find
    def test_mixed_operations(self, func: FUNC_T) -> None:
        queries = [
            ("add", "10", "a"),
            ("find", "10", ""),
            ("add", "10", "b"),
            ("find", "10", ""),
            ("del", "10", ""),
            ("find", "10", ""),
            ("add", "20", "c"),
            ("del", "10", ""),  # уже удалён
            ("find", "20", ""),
        ]
        expected = ["a", "b", "not found", "c"]
        assert func(queries) == expected

    # Много запросов (на запас прочности)
    def test_many_queries(self, func: FUNC_T) -> None:
        queries = []
        expected = []
        # Добавим 50 номеров
        for i in range(50):
            queries.append(("add", str(i), f"name{i}"))  # noqa: PERF401
        # Поиск 25 добавленных + 5 несуществующих
        for i in range(25):
            queries.append(("find", str(i), ""))
            expected.append(f"name{i}")
        for i in range(50, 55):
            queries.append(("find", str(i), ""))
            expected.append("not found")
        # Удалим 10 номеров
        for i in range(10):
            queries.append(("del", str(i), ""))  # noqa: PERF401
        # Снова поиск удалённых и оставшихся
        for i in range(15):
            queries.append(("find", str(i), ""))
            if i < 10:
                expected.append("not found")
            else:
                expected.append(f"name{i}")
        assert func(queries) == expected

    # Проверка, что при открытой адресации коллизии не ломают логику
    # (хеш-функция h(key) = key * 11 всегда даёт коллизию для ключей 1 и 6 при размере 5)
    def test_collision_handling(self, func: FUNC_T) -> None:
        # Для прямого адреса коллизий нет, тест всё равно корректен
        # Готовим запросы с capacity = 5 (len(queries) будет 7, но внутри open address
        # передаётся len(queries) как размер таблицы)
        queries = [
            ("add", "1", "One"),
            ("add", "6", "Six"),  # h(1)=11%7=4, h(6)=66%7=3? Разные. Создадим коллизию иначе.
        ]
        # Подберём ключи так, чтобы h(key) % len(queries) совпадали.
        # Пусть len(queries) = 5, тогда h(k)=k*11 %5. h(1)=1, h(6)=11%5=1 -> коллизия.
        # Для этого сформируем список запросов длиной 5.
        queries = [
            ("add", "1", "First"),
            ("add", "6", "Second"),  # оба h%5=1
            ("find", "1", ""),
            ("find", "6", ""),
            ("find", "0", ""),
        ]
        expected = ["First", "Second", "not found"]
        # Примечание: для прямого адреса этот тест тривиален, для открытой адресации проверяем,
        # что оба ключа находятся, несмотря на коллизию.
        assert func(queries) == expected
