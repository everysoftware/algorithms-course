import pytest

# Предполагаем, что класс ChainingHashMap определён в модуле src.hash_tables.chaining
from src.hash_tables.chaining import ChainingHashMap

# ==============================
# Вспомогательные хеш-функции
# ==============================


def hash_identity(key: int) -> int:
    """Хеш-функция, возвращающая сам ключ."""
    return key


def hash_constant(key: int) -> int:
    """Хеш-функция, всегда возвращающая 0 (максимальные коллизии)."""
    return 0


def hash_mod_10(key: int) -> int:
    """Пример хеш-функции с ограниченным диапазоном."""
    return key % 10


# ==============================
# Тесты
# ==============================


class TestChainingHashMap:
    # ----------------------------------------------------------------
    # Базовая функциональность
    # ----------------------------------------------------------------

    def test_empty_map(self) -> None:
        m = ChainingHashMap[int, str](hash_identity, capacity=4)
        assert m.size == 0
        assert m.get(1) is None
        # Проверка, что delete выбрасывает KeyError
        with pytest.raises(KeyError):
            m.delete(1)

    @pytest.mark.parametrize("hash_func", [hash_identity, hash_constant])
    def test_add_and_get(self, hash_func) -> None:
        m = ChainingHashMap[int, str](hash_func, capacity=8)
        m.add(10, "Alice")
        assert m.get(10) == "Alice"
        assert m.size == 1

    @pytest.mark.parametrize("hash_func", [hash_identity, hash_constant])
    def test_add_update_value(self, hash_func) -> None:
        m = ChainingHashMap[int, str](hash_func, capacity=4)
        m.add(42, "old")
        m.add(42, "new")
        assert m.get(42) == "new"
        # Размер не должен измениться при обновлении
        assert m.size == 1

    @pytest.mark.parametrize("hash_func", [hash_identity, hash_constant])
    def test_delete_existing(self, hash_func) -> None:
        m = ChainingHashMap[int, str](hash_func, capacity=4)
        m.add(7, "seven")
        m.delete(7)
        assert m.get(7) is None
        assert m.size == 0
        with pytest.raises(KeyError):
            m.delete(7)

    def test_delete_non_existing(self) -> None:
        m = ChainingHashMap[int, str](hash_identity, capacity=4)
        with pytest.raises(KeyError) as exc_info:
            m.delete(99)
        # Проверяем, что исключение содержит ключ
        assert exc_info.value.args[0] == 99

    @pytest.mark.parametrize("hash_func", [hash_identity, hash_constant])
    def test_multiple_operations(self, hash_func) -> None:
        m = ChainingHashMap[int, str](hash_func, capacity=4)
        # Добавляем три элемента
        m.add(1, "one")
        m.add(2, "two")
        m.add(3, "three")
        assert m.size == 3

        # Обновляем один
        m.add(2, "TWO")
        assert m.get(2) == "TWO"
        assert m.size == 3  # размер не изменился

        # Удаляем другой
        m.delete(3)
        assert m.get(3) is None
        assert m.size == 2

        # Пытаемся удалить несуществующий
        with pytest.raises(KeyError):
            m.delete(3)

        # Проверяем оставшиеся
        assert m.get(1) == "one"
        assert m.get(2) == "TWO"

    # ----------------------------------------------------------------
    # Коллизии
    # ----------------------------------------------------------------

    def test_collision_same_bucket(self) -> None:
        """Все ключи попадают в бакет 0, цепочка растёт."""
        m = ChainingHashMap[int, str](hash_constant, capacity=4)
        m.add(5, "five")
        m.add(8, "eight")
        m.add(13, "thirteen")
        assert m.size == 3
        # Все три должны быть доступны
        assert m.get(5) == "five"
        assert m.get(8) == "eight"
        assert m.get(13) == "thirteen"

        # Удаляем элемент из середины цепочки
        m.delete(8)
        assert m.get(8) is None
        assert m.size == 2
        # Оставшиеся на месте
        assert m.get(5) == "five"
        assert m.get(13) == "thirteen"

    def test_collision_with_different_hash_values(self) -> None:
        """Коллизия из-за остатка от деления на capacity."""
        # При capacity=4 hash=1 и hash=5 оба дают индекс 1.
        m = ChainingHashMap[int, str](lambda k: k, capacity=4)
        m.add(1, "one")
        m.add(5, "five")
        assert m.get(1) == "one"
        assert m.get(5) == "five"
        # Удаляем первый, второй остаётся
        m.delete(1)
        assert m.get(1) is None
        assert m.get(5) == "five"
        assert m.size == 1

    # ----------------------------------------------------------------
    # Рехэширование
    # ----------------------------------------------------------------

    def test_rehash_triggers(self) -> None:
        """При факторе загрузки >= 0.75 должно происходить расширение."""
        # Начальная capacity = 4, REHASH_FACTOR = 0.75 => порог size=3.
        m = ChainingHashMap[int, str](lambda k: k, capacity=4)
        # Добавляем 3 элемента – рехэша ещё нет (size/capacity = 0.75)
        for i in range(3):
            m.add(i, str(i))
        assert m.capacity == 4
        assert m.size == 3

        # Четвёртый элемент вызывает рехэш (size станет 4, capacity станет 8)
        m.add(3, "three")
        assert m.capacity == 8
        assert m.size == 4

        # Все предыдущие должны быть доступны
        for i in range(3):
            assert m.get(i) == str(i)
        assert m.get(3) == "three"
        assert m.get(99) is None

    def test_rehash_preserves_collisions(self) -> None:
        """После рехэша элементы из переполненных цепочек остаются доступны."""
        # Все ключи идут в бакет 0 из-за хеш-функции, вызываем рехэш.
        m = ChainingHashMap[int, str](hash_constant, capacity=4)
        for i in range(10):
            m.add(i, f"val{i}")
        assert m.capacity > 4  # точно был рехэш
        assert m.size == 10
        for i in range(10):
            assert m.get(i) == f"val{i}"

        # Удаление пары элементов после рехэша
        m.delete(0)
        m.delete(9)
        assert m.get(0) is None
        assert m.get(9) is None
        assert m.size == 8
        for i in range(1, 9):
            assert m.get(i) == f"val{i}"

    def test_rehash_with_low_initial_capacity(self) -> None:
        """Проверка поведения при начальной capacity=1."""
        m = ChainingHashMap[int, str](hash_identity, capacity=1)
        # Первое добавление: size=0, 0/1 < 0.75, рехэша нет.
        m.add(1, "one")
        assert m.capacity == 1  # ёмкость не изменилась
        assert m.size == 1
        assert m.get(1) == "one"

        # Второе добавление: size=1, 1/1 >= 0.75, срабатывает рехэш до вставки.
        m.add(2, "two")
        assert m.capacity == 2  # увеличилась в 2 раза
        assert m.size == 2
        assert m.get(1) == "one"
        assert m.get(2) == "two"

    # ----------------------------------------------------------------
    # Различные типы ключей и значений
    # ----------------------------------------------------------------

    def test_string_keys(self) -> None:
        """Проверка работы со строками."""

        def str_len_hash(s: str) -> int:
            return len(s)

        m = ChainingHashMap[str, float](str_len_hash, capacity=8)
        m.add("hello", 1.23)
        m.add("world", 4.56)
        assert m.get("hello") == 1.23
        assert m.get("world") == 4.56
        m.delete("hello")
        assert m.get("hello") is None
        with pytest.raises(KeyError):
            m.delete("hello")

    def test_custom_class_key(self) -> None:
        """Проверка, что класс корректно работает с ключами-объектами."""

        class Point:
            def __init__(self, x: int, y: int) -> None:
                self.x = x
                self.y = y

            def __eq__(self, other) -> bool:
                return self.x == other.x and self.y == other.y

            def __hash__(self) -> int:
                return self.x + self.y

        def point_hash(p: Point) -> int:
            return hash(p)

        m = ChainingHashMap[Point, str](point_hash, capacity=4)
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        m.add(p1, "first")
        m.add(p2, "second")
        assert m.get(p1) == "first"
        # Ключ с такими же координатами должен считаться тем же (если __eq__ и hash)
        assert m.get(Point(1, 2)) == "first"
        m.delete(p2)
        assert m.get(p2) is None
        assert m.size == 1

    # ----------------------------------------------------------------
    # Краевые случаи
    # ----------------------------------------------------------------

    def test_large_number_of_items(self) -> None:
        """Стресс-тест: 1000 элементов с постоянной хеш-функцией."""
        m = ChainingHashMap[int, int](hash_constant, capacity=4)
        n = 1000
        for i in range(n):
            m.add(i, i * 10)
        assert m.size == n
        # Выборочная проверка
        for i in range(0, n, 100):
            assert m.get(i) == i * 10

        # Удалим все чётные
        for i in range(0, n, 2):
            m.delete(i)
        assert m.size == n // 2
        # Проверим, что нечётные остались
        for i in range(1, n, 2):
            assert m.get(i) == i * 10
        # Попытка удалить уже удалённый
        with pytest.raises(KeyError):
            m.delete(0)
