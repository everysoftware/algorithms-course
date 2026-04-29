from src.dsu.auto_analysis import auto_analysis

# --------------------
# БАЗОВЫЕ СЛУЧАИ
# --------------------


def test_no_constraints() -> None:
    assert auto_analysis(5, 0, 0, [], []) is True


def test_only_equals() -> None:
    n = 4
    equals = [(1, 2), (2, 3), (3, 4)]
    assert auto_analysis(n, len(equals), 0, equals, []) is True


def test_only_not_equals() -> None:
    n = 4
    not_equals = [(1, 2), (2, 3), (3, 4)]
    assert auto_analysis(n, 0, len(not_equals), [], not_equals) is True


# --------------------
# ПРОТИВОРЕЧИЯ
# --------------------


def test_simple_conflict() -> None:
    n = 2
    equals = [(1, 2)]
    not_equals = [(1, 2)]
    assert auto_analysis(n, 1, 1, equals, not_equals) is False


def test_indirect_conflict() -> None:
    n = 3
    equals = [(1, 2), (2, 3)]
    not_equals = [(1, 3)]
    assert auto_analysis(n, 2, 1, equals, not_equals) is False


def test_large_conflict_chain() -> None:
    n = 5
    equals = [(1, 2), (2, 3), (3, 4), (4, 5)]
    not_equals = [(1, 5)]
    assert auto_analysis(n, 4, 1, equals, not_equals) is False


# --------------------
# КОРРЕКТНЫЕ СЛУЧАИ
# --------------------


def test_separate_components() -> None:
    n = 4
    equals = [(1, 2), (3, 4)]
    not_equals = [(1, 3)]
    assert auto_analysis(n, 2, 1, equals, not_equals) is True


def test_multiple_components() -> None:
    n = 6
    equals = [(1, 2), (3, 4), (5, 6)]
    not_equals = [(1, 3), (2, 5), (4, 6)]
    assert auto_analysis(n, 3, 3, equals, not_equals) is True


# --------------------
# САМОССЫЛКИ
# --------------------


def test_self_equality() -> None:
    n = 3
    equals = [(1, 1), (2, 2)]
    assert auto_analysis(n, 2, 0, equals, []) is True


def test_self_inequality() -> None:
    n = 3
    not_equals = [(1, 1)]
    assert auto_analysis(n, 0, 1, [], not_equals) is False


# --------------------
# ДУБЛИРУЮЩИЕ ОГРАНИЧЕНИЯ
# --------------------


def test_duplicate_equals() -> None:
    n = 3
    equals = [(1, 2), (1, 2), (2, 1)]
    assert auto_analysis(n, 3, 0, equals, []) is True


def test_duplicate_not_equals() -> None:
    n = 3
    not_equals = [(1, 2), (1, 2), (2, 1)]
    assert auto_analysis(n, 0, 3, [], not_equals) is True


# --------------------
# СМЕШАННЫЕ СЛОЖНЫЕ СЛУЧАИ
# --------------------


def test_complex_valid() -> None:
    n = 6
    equals = [(1, 2), (2, 3), (4, 5)]
    not_equals = [(1, 4), (3, 6), (5, 6)]
    assert auto_analysis(n, 3, 3, equals, not_equals) is True


def test_complex_invalid() -> None:
    n = 6
    equals = [(1, 2), (2, 3), (3, 4)]
    not_equals = [(1, 4), (2, 5)]
    assert auto_analysis(n, 3, 2, equals, not_equals) is False


# --------------------
# ГРАНИЧНЫЕ СЛУЧАИ
# --------------------


def test_single_variable() -> None:
    assert auto_analysis(1, 0, 0, [], []) is True


def test_single_variable_conflict() -> None:
    assert auto_analysis(1, 0, 1, [], [(1, 1)]) is False


# --------------------
# СТРЕСС (логический)
# --------------------


def test_long_chain_no_conflict() -> None:
    n = 1000
    equals = [(i, i + 1) for i in range(1, n)]
    not_equals = [(1, n + 1)] if n + 1 <= n else []
    assert auto_analysis(n, len(equals), len(not_equals), equals, not_equals) is True


def test_long_chain_with_conflict() -> None:
    n = 1000
    equals = [(i, i + 1) for i in range(1, n)]
    not_equals = [(1, n)]
    assert auto_analysis(n, len(equals), 1, equals, not_equals) is False
