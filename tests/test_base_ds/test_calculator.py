import pytest

from base_ds import split_by_tokens, get_postfix_notation, evaluate_postfix, calculator


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Тестовый случай 1: Простое выражение без скобок.
        ("2+2", ["2", "+", "2"]),
        # Тестовый случай 2: Выражение со скобками.
        ("(1+2)*3", ["(", "1", "+", "2", ")", "*", "3"]),
        # Тестовый случай 3: Выражение с десятичными числами.
        ("3.14*2", ["3.14", "*", "2"]),
        # Тестовый случай 4: Выражение с пробелами.
        (" 2 + 2 ", ["2", "+", "2"]),
        # Тестовый случай 5: Пустое выражение.
        ("", []),
    ],
)
def test_split_by_tokens(expression: str, expected: list[str]):
    assert split_by_tokens(expression) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Тестовый случай 1: Простое выражение без скобок.
        ("2 + 2", "2 2 +"),
        # Тестовый случай 2: Выражение со скобками.
        ("( 1 + 2 ) * 3", "1 2 + 3 *"),
        # Тестовый случай 3: Выражение с различными операторами.
        ("2 * 3 + 4", "2 3 * 4 +"),
        # Тестовый случай 4: Пустое выражение.
        ("", ""),
    ],
)
def test_get_postfix_notation(expression: str, expected: str):
    assert get_postfix_notation(expression) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Тестовый случай 1: Простое выражение без скобок.
        ("2 2 +", 4.0),
        # Тестовый случай 2: Выражение со скобками.
        ("1 2 + 3 *", 9.0),
        # Тестовый случай 3: Выражение с различными операторами.
        ("2 3 * 4 +", 10.0),
        # Тестовый случай 4: Пустое выражение.
        ("", 0.0),
    ],
)
def test_evaluate_postfix(expression: str, expected: float):
    assert evaluate_postfix(expression) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Тест из условия задачи.
        ("(1+2)*4+3", ("1 2 + 4 * 3 +", 15.0)),
        # Тестовый случай 1: Простое выражение без скобок.
        ("2+2", ("2 2 +", 4.0)),
        # Тестовый случай 2: Выражение со скобками.
        ("(1+2)*3", ("1 2 + 3 *", 9.0)),
        # Тестовый случай 3: Выражение с различными операторами.
        ("2*3+4", ("2 3 * 4 +", 10.0)),
        # Тестовый случай 4: Пустое выражение.
        ("", ("", 0.0)),
    ],
)
def test_calculator(expression: str, expected: tuple[str, float]):
    assert calculator(expression) == expected
