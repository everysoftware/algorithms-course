import pytest

from src.b_base_ds.calculator import (
    split_by_tokens,
    get_postfix_notation,
    evaluate_postfix,
    calculator,
)


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Базовый случай.
        ("2+2", ["2", "+", "2"]),
        # Скобки.
        ("(1+2)*3", ["(", "1", "+", "2", ")", "*", "3"]),
        # Числа с плавающей точкой.
        ("3.14*2", ["3.14", "*", "2"]),
        # Пробелы.
        (" 2 + 2 ", ["2", "+", "2"]),
        # Пустое выражение.
        ("", []),
        # Отрицательные числа и пробелы.
        ("1-(     -2)", ["1", "-", "(", "-", "2", ")"]),
    ],
)
def test_split_by_tokens(expression: str, expected: list[str]) -> None:
    assert split_by_tokens(expression) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Тестовый случай 1: Простое выражение без скобок.
        ("2 + 2", "2 2 +"),
        # Тестовый случай 2: Выражение со скобками.
        ("( 1 + 2 ) * 3", "1 2 + 3 *"),
        # Тестовый случай 3: Выражение с различными операторами.
        ("4 + 2 * 3", "4 2 3 * +"),
        # Тестовый случай 4: Пустое выражение.
        ("", ""),
    ],
)
def test_get_postfix_notation(expression: str, expected: str) -> None:
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
def test_evaluate_postfix(expression: str, expected: float) -> None:
    assert evaluate_postfix(expression) == expected


@pytest.mark.parametrize(
    "expression, expected",
    [
        # Тест из условия задачи.
        ("(1+2)*4+3", 15.0),
        # Тестовый случай 1: Простое выражение без скобок.
        ("2+2", 4.0),
        # Тестовый случай 2: Выражение со скобками.
        ("(1+2)*3", 9.0),
        # Тестовый случай 3: Выражение с различными операторами.
        ("4+2*3", 10.0),
        # Тестовый случай 4: Пустое выражение.
        ("", 0.0),
        # Тестовый случай 5: Выражение с отрицательными числами.
        ("1-(     -2)", 3.0),
    ],
)
def test_calculator(expression: str, expected: float) -> None:
    assert calculator(expression) == expected
