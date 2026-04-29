from src.dsu.max_dsu import MaxDSU
from src.dsu.table_union import table_union

# --------------------
# БАЗОВЫЕ СЛУЧАИ
# --------------------


def test_single_element() -> None:
    assert table_union([5], [(1, 1)]) == [5]


def test_two_elements_merge() -> None:
    assert table_union([1, 2], [(1, 2)]) == [3]


def test_self_union() -> None:
    assert table_union([10, 20], [(1, 1), (2, 2)]) == [20, 20]


# --------------------
# ПРИМЕРЫ ИЗ УСЛОВИЯ
# --------------------


def test_example_1() -> None:
    sizes = [1, 1, 1, 1, 1]
    queries = [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]
    assert table_union(sizes, queries) == [2, 2, 3, 5, 5]


def test_example_2() -> None:
    sizes = [10, 0, 5, 0, 3, 3]
    queries = [(6, 6), (6, 5), (5, 4), (4, 3)]
    assert table_union(sizes, queries) == [10, 10, 10, 11]


# --------------------
# ЦЕПОЧКИ
# --------------------


def test_linear_chain() -> None:
    sizes = [1, 2, 3, 4]
    queries = [(1, 2), (2, 3), (3, 4)]
    assert table_union(sizes, queries) == [4, 6, 10]


def test_reverse_chain() -> None:
    sizes = [1, 2, 3, 4]
    queries = [(4, 3), (3, 2), (2, 1)]
    assert table_union(sizes, queries) == [7, 9, 10]


# --------------------
# ЗВЕЗДА
# --------------------


def test_star() -> None:
    sizes = [1, 1, 1, 1, 1]
    queries = [(1, 2), (1, 3), (1, 4), (1, 5)]
    assert table_union(sizes, queries) == [2, 3, 4, 5]


# --------------------
# ПОВТОРНЫЕ ОБЪЕДИНЕНИЯ
# --------------------


def test_repeated_unions() -> None:
    sizes = [1, 2, 3]
    queries = [(1, 2), (1, 2), (2, 1), (2, 3)]
    assert table_union(sizes, queries) == [3, 3, 3, 6]


# --------------------
# КОСВЕННЫЕ СВЯЗИ
# --------------------


def test_indirect_connections() -> None:
    sizes = [1, 2, 3]
    queries = [(1, 2), (2, 3), (1, 3)]
    assert table_union(sizes, queries) == [3, 6, 6]


# --------------------
# НУЛЕВЫЕ ЗНАЧЕНИЯ
# --------------------


def test_all_zero() -> None:
    sizes = [0, 0, 0]
    queries = [(1, 2), (2, 3)]
    assert table_union(sizes, queries) == [0, 0]


def test_mixed_zero() -> None:
    sizes = [0, 5, 0, 3]
    queries = [(1, 2), (3, 4), (1, 3)]
    assert table_union(sizes, queries) == [5, 5, 8]


# --------------------
# ПРОВЕРКА curr_max
# --------------------


def test_curr_max_updates() -> None:
    dsu = MaxDSU([1, 2, 3])
    assert dsu.curr_max == 3

    dsu.union(0, 1)
    assert dsu.curr_max == 3

    dsu.union(1, 2)
    assert dsu.curr_max == 6


# --------------------
# БОЛЬШИЕ ТЕСТЫ
# --------------------


def test_large_chain() -> None:
    n = 1000
    sizes = [1] * n
    queries = [(i, i + 1) for i in range(1, n)]
    result = table_union(sizes, queries)
    assert result[-1] == n


def test_large_star() -> None:
    n = 1000
    sizes = [1] * n
    queries = [(1, i) for i in range(2, n + 1)]
    result = table_union(sizes, queries)
    assert result[-1] == n


# --------------------
# СЛОЖНЫЙ СЦЕНАРИЙ
# --------------------


def test_complex_case() -> None:
    sizes = [5, 1, 1, 1, 10]
    queries = [
        (2, 3),  # 2
        (3, 4),  # 3
        (1, 2),  # 8
        (5, 1),  # 18
    ]
    assert table_union(sizes, queries) == [10, 10, 10, 18]
