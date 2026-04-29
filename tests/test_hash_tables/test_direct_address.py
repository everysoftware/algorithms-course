import pytest

from src.hash_tables.direct_address import DirectAddressMap


# ---------------------------------------------------------------------------
# Тесты конструктора
# ---------------------------------------------------------------------------
class TestConstructor:
    def test_valid_size(self) -> None:
        m = DirectAddressMap[int](5)
        assert len(m._data) == 5

    def test_zero_size(self) -> None:
        m = DirectAddressMap[str](0)
        assert len(m._data) == 0

    def test_negative_size_raises(self) -> None:
        with pytest.raises(ValueError):  # noqa: PT011
            DirectAddressMap[int](-1)


# ---------------------------------------------------------------------------
# Тесты add
# ---------------------------------------------------------------------------
class TestAdd:
    def test_add_single(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(3, 42)
        assert m.get(3) == 42

    def test_add_overwrite(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(3, 42)
        m.add(3, 99)
        assert m.get(3) == 99

    def test_add_none_value(self) -> None:
        """None должен сохраняться как обычное значение, а не интерпретироваться как отсутствие."""
        m = DirectAddressMap[int | None](10)
        m.add(5, None)
        assert m.get(5) is None
        # Убедимся, что ключ действительно присутствует (не возвращает дефолт)
        assert m.get(5, default=123) is None  # вернёт None, а не "missing"

    def test_add_out_of_bounds_left(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError):
            m.add(-1, 10)

    def test_add_out_of_bounds_right(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError):
            m.add(5, 10)  # max index = 4

    def test_add_to_zero_size_map(self) -> None:
        m = DirectAddressMap[int](0)
        with pytest.raises(KeyError):
            m.add(0, 1)

    def test_add_multiple_keys(self) -> None:
        m = DirectAddressMap[str](4)
        m.add(0, "a")
        m.add(3, "b")
        assert m.get(0) == "a"
        assert m.get(3) == "b"


# ---------------------------------------------------------------------------
# Тесты get
# ---------------------------------------------------------------------------
class TestGet:
    def test_get_existing(self) -> None:
        m = DirectAddressMap[str](5)
        m.add(2, "hello")
        assert m.get(2) == "hello"

    def test_get_missing_returns_none(self) -> None:
        m = DirectAddressMap[int](5)
        assert m.get(2) is None

    def test_get_missing_returns_custom_default(self) -> None:
        m = DirectAddressMap[int](5)
        assert m.get(2, -1) == -1

    def test_get_with_explicit_none_default(self) -> None:
        m = DirectAddressMap[int](5)
        assert m.get(2, None) is None

    def test_get_out_of_bounds_left(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError):
            m.get(-1)

    def test_get_out_of_bounds_right(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError):
            m.get(5)

    def test_get_from_zero_size_map(self) -> None:
        m = DirectAddressMap[int](0)
        with pytest.raises(KeyError):
            m.get(0)

    def test_get_after_delete_returns_none(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(7, 100)
        m.delete(7)
        assert m.get(7) is None

    def test_get_after_delete_with_default(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(7, 100)
        m.delete(7)
        assert m.get(7, 123) == 123


# ---------------------------------------------------------------------------
# Тесты delete
# ---------------------------------------------------------------------------
class TestDelete:
    def test_delete_existing(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(4, 42)
        m.delete(4)
        # после удаления ключ не должен находиться
        assert m.get(4) is None

    def test_delete_nonexistent_raises_keyerror(self) -> None:
        m = DirectAddressMap[int](10)
        with pytest.raises(KeyError):
            m.delete(5)

    def test_delete_twice_raises_keyerror(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(1, 10)
        m.delete(1)
        with pytest.raises(KeyError):
            m.delete(1)  # уже пусто

    def test_delete_out_of_bounds_left(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError):
            m.delete(-1)

    def test_delete_out_of_bounds_right(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError):
            m.delete(5)

    def test_delete_from_zero_size_map(self) -> None:
        m = DirectAddressMap[int](0)
        with pytest.raises(KeyError):
            m.delete(0)

    def test_delete_preserves_other_keys(self) -> None:
        m = DirectAddressMap[str](10)
        m.add(1, "one")
        m.add(2, "two")
        m.delete(1)
        assert m.get(2) == "two"
        assert m.get(1) is None

    def test_delete_allows_reinsertion(self) -> None:
        """Убедимся, что после удаления ячейка становится полностью пустой
        и в неё можно снова добавить значение."""
        m = DirectAddressMap[int](10)
        m.add(3, 100)
        m.delete(3)
        m.add(3, 200)
        assert m.get(3) == 200

    def test_delete_then_store_none(self) -> None:
        """После удаления можно сохранить None и получить его."""
        m = DirectAddressMap[int | None](10)
        m.add(3, 100)
        m.delete(3)
        m.add(3, None)
        assert m.get(3) is None
        assert m.get(3, 123) is None  # убеждаемся, что это не default


# ---------------------------------------------------------------------------
# Тесты на sentinel и None
# ---------------------------------------------------------------------------
class TestSentinelNoneSeparation:
    def test_none_is_not_emtpy(self) -> None:
        m = DirectAddressMap[int | None](5)
        m.add(0, None)
        # ключ существует, поэтому get не возвращает default
        assert m.get(0, 123) is None
        # удаление существующего ключа с None работает
        m.delete(0)
        with pytest.raises(KeyError):
            m.delete(0)  # теперь пусто

    def test_emtpy_slot_returns_default(self) -> None:
        m = DirectAddressMap[int | None](5)
        # слот пуст, get возвращает default
        assert m.get(0, 123) == 123
        # default None работает и возвращает None, но это именно default
        assert m.get(0, None) is None


# ---------------------------------------------------------------------------
# Тесты на корректность исключений
# ---------------------------------------------------------------------------
class TestExceptions:
    def test_keyerror_contains_key(self) -> None:
        m = DirectAddressMap[int](5)
        with pytest.raises(KeyError) as exc_info:
            m.delete(99)
        assert exc_info.value.args[0] == 99

    def test_keyerror_out_of_bounds_contains_key(self) -> None:
        m = DirectAddressMap[int](3)
        with pytest.raises(KeyError) as exc_info:
            m.add(-1, 0)
        assert exc_info.value.args[0] == -1


# ---------------------------------------------------------------------------
# Тесты граничных ключей (0 и size-1)
# ---------------------------------------------------------------------------
class TestBoundaryKeys:
    def test_key_zero_works(self) -> None:
        m = DirectAddressMap[int](10)
        m.add(0, 123)
        assert m.get(0) == 123
        m.delete(0)
        assert m.get(0) is None

    def test_key_max_works(self) -> None:
        m = DirectAddressMap[int](10)
        max_key = 9
        m.add(max_key, 999)
        assert m.get(max_key) == 999
        m.delete(max_key)
        with pytest.raises(KeyError):
            m.delete(max_key)

    def test_key_max_plus_one_raises(self) -> None:
        m = DirectAddressMap[int](5)  # keys 0..4
        with pytest.raises(KeyError):
            m.add(5, 1)
