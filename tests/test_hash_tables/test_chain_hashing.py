from collections import deque

import pytest

from src.hash_tables.chain_hashing import ChainingSet, chain_hashing, h


# ==============================
# Тесты для хеш-функции h
# ==============================
def test_hash_function_deterministic() -> None:
    assert h("abc") == h("abc")


def test_hash_function_different_strings() -> None:
    # Ожидаем, что разные строки дают разные значения (не обязательно, но вероятно)
    # Здесь просто проверяем, что функция не падает и возвращает целое
    assert isinstance(h("hello"), int)


def test_hash_function_empty_string() -> None:
    assert h("") == 0  # по логике схема Горнера с пустой строкой даст 0


# ==============================
# Тесты для ChainingSet
# ==============================
class TestChainingSetBasic:
    @pytest.fixture()
    def empty_set(self) -> ChainingSet[str]:
        return ChainingSet[str](h, capacity=4)

    def test_empty_table_creation(self, empty_set: ChainingSet[str]) -> None:
        assert empty_set.capacity == 4
        assert len(empty_set.table) == 4
        assert all(isinstance(chain, deque) for chain in empty_set.table)
        assert all(len(chain) == 0 for chain in empty_set.table)

    def test_add_single(self, empty_set: ChainingSet[str]) -> None:
        empty_set.add("abc")
        assert empty_set.find("abc") is True
        assert empty_set.find("xyz") is False

    def test_add_duplicate_ignored(self, empty_set: ChainingSet[str]) -> None:
        empty_set.add("abc")
        empty_set.add("abc")
        # Размер цепочки должен остаться 1
        idx = h("abc") % 4
        assert len(empty_set.table[idx]) == 1

    def test_add_multiple_same_hash(self, empty_set: ChainingSet[str]) -> None:
        # Используем модифицированную хеш-функцию с постоянным значением
        const_set = ChainingSet[str](lambda s: 0, capacity=4)
        const_set.add("first")
        const_set.add("second")
        const_set.add("third")
        idx = 0
        chain = const_set.table[idx]
        assert len(chain) == 3
        # Порядок: добавлялись first, second, third; каждый в начало.
        # После всех вставок должно быть: third, second, first
        assert list(chain) == ["third", "second", "first"]

    def test_find_existing(self, empty_set: ChainingSet[str]) -> None:
        empty_set.add("key")
        assert empty_set.find("key") is True

    def test_find_non_existing(self, empty_set: ChainingSet[str]) -> None:
        assert empty_set.find("ghost") is False

    def test_delete_existing(self, empty_set: ChainingSet[str]) -> None:
        empty_set.add("to_delete")
        empty_set.delete("to_delete")
        assert empty_set.find("to_delete") is False

    def test_delete_non_existing_silent(self, empty_set: ChainingSet[str]) -> None:
        # Не должно вызывать исключения
        empty_set.delete("ghost")
        # Состояние не меняется
        assert empty_set.find("ghost") is False

    def test_delete_from_empty_chain(self, empty_set: ChainingSet[str]) -> None:
        # Даже если цепочка пуста, удаление не вызывает ошибки
        empty_set.delete("anything")
        assert True  # не упали

    def test_get_chain_normal(self, empty_set: ChainingSet[str]) -> None:
        empty_set.add("a")
        empty_set.add("b")
        # a и b могут оказаться в разных цепочках; проверим содержимое
        # Лучше создать контролируемую хеш-функцию
        const_set = ChainingSet[str](lambda s: 0, capacity=2)
        const_set.add("1")
        const_set.add("2")
        const_set.add("3")
        assert const_set.get_chain(0) == "3 2 1"
        assert const_set.get_chain(1) == ""

    def test_get_chain_out_of_bounds(self, empty_set: ChainingSet[str]) -> None:
        assert empty_set.get_chain(-1) == ""
        assert empty_set.get_chain(4) == ""
        assert empty_set.get_chain(100) == ""

    def test_get_chain_non_string_elements(self) -> None:
        int_set = ChainingSet[int](lambda x: x % 2, capacity=2)
        int_set.add(10)
        int_set.add(20)
        # проверяем str(x) в выводе
        assert int_set.get_chain(0) == "20 10"  # 20 и 10 четные, порядок: 20 добавлен позже -> в начало

    def test_delete_removes_only_one_occurrence(self, empty_set: ChainingSet[str]) -> None:
        # Так как дубликаты не добавляются, проверяем, что remove удаляет именно этот элемент
        const_set = ChainingSet[str](lambda s: 0, capacity=1)
        const_set.add("x")
        const_set.add("y")
        const_set.delete("x")
        assert list(const_set.table[0]) == ["y"]

    def test_capacity_initialization_default(self) -> None:
        s = ChainingSet[str](h)
        assert s.capacity == 8


# ==============================
# Тесты для chain_hashing (интеграционные)
# ==============================
class TestChainHashingIntegration:
    def test_empty_queries(self) -> None:
        assert chain_hashing(5, []) == []

    def test_unknown_command_raises(self) -> None:
        with pytest.raises(NotImplementedError):
            chain_hashing(5, [("invalid", "data")])

    def test_example_from_problem(self) -> None:
        m = 5
        queries = [
            ("add", "world"),
            ("add", "HellO"),
            ("check", "4"),
            ("find", "World"),
            ("find", "world"),
            ("del", "world"),
            ("check", "4"),
            ("del", "HellO"),
            ("add", "luck"),
            ("add", "GooD"),
            ("check", "2"),
            ("del", "good"),
        ]
        result = chain_hashing(m, queries)
        expected = [
            "HellO world",
            "no",
            "yes",
            "HellO",
            "GooD luck",
        ]
        assert result == expected

    def test_second_example_problem(self) -> None:
        m = 4
        queries = [
            ("add", "test"),
            ("add", "test"),
            ("find", "test"),
            ("del", "test"),
            ("find", "test"),
            ("find", "Test"),
            ("add", "Test"),
            ("find", "Test"),
        ]
        result = chain_hashing(m, queries)
        expected = [
            "yes",
            "no",
            "no",
            "yes",
        ]
        assert result == expected

    def test_third_example_problem(self) -> None:
        m = 3
        queries = [
            ("check", "0"),
            ("find", "help"),
            ("add", "help"),
            ("add", "del"),
            ("add", "add"),
            ("find", "add"),
            ("find", "del"),
            ("del", "del"),
            ("find", "del"),
            ("check", "0"),
            ("check", "1"),
            ("check", "2"),
        ]
        result = chain_hashing(m, queries)
        expected = [
            "",
            "no",
            "yes",
            "yes",
            "no",
            "",
            "add help",
            "",
        ]
        assert result == expected

    def test_check_boundaries(self) -> None:
        # m=1
        queries = [("check", "0"), ("add", "a"), ("check", "0"), ("check", "1")]
        result = chain_hashing(1, queries)
        assert result == ["", "a", ""]  # check 1 за границей -> ""

    def test_add_and_find_multiple(self) -> None:
        m = 10
        queries = [("add", f"key{i}") for i in range(20)]
        queries += [("find", f"key{i}") for i in range(20)]
        queries += [("find", "missing")]
        expected = ["yes"] * 20 + ["no"]
        chain_hashing(m, queries[20:])  # только find команды
        # нужно собрать все find команды
        all_queries = queries
        find_results = chain_hashing(m, all_queries)
        # первые 20 add ничего не выводят
        assert find_results == expected

    def test_del_ignore_missing(self) -> None:
        m = 5
        queries = [("del", "x"), ("find", "x"), ("add", "x"), ("find", "x")]
        result = chain_hashing(m, queries)
        assert result == ["no", "yes"]
