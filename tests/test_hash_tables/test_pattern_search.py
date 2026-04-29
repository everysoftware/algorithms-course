import random
import string

# Функция теперь должна принимать p и x (см. ниже)
from src.hash_tables.pattern_search import rabin_karp


# ------------------------------------------------------------
# 1. Базовые проверки
# ------------------------------------------------------------
def test_simple_case() -> None:
    assert rabin_karp("aba", "abacaba") == [0, 4]


def test_single_match() -> None:
    assert rabin_karp("Test", "testTesttesT") == [4]


def test_no_match() -> None:
    assert rabin_karp("abc", "defgh") == []


# ------------------------------------------------------------
# 2. Перекрывающиеся вхождения
# ------------------------------------------------------------
def test_overlapping() -> None:
    assert rabin_karp("aaa", "aaaaa") == [0, 1, 2]


def test_overlapping_two_chars() -> None:
    assert rabin_karp("aa", "aaa") == [0, 1]


def test_full_overlap() -> None:
    assert rabin_karp("a", "aaaa") == [0, 1, 2, 3]


def test_overlapping_long_pattern() -> None:
    assert rabin_karp("aaaaa", "baaaaaaa") == [1, 2, 3]


# ------------------------------------------------------------
# 3. Крайние случаи длин
# ------------------------------------------------------------
def test_pattern_equals_text() -> None:
    assert rabin_karp("abc", "abc") == [0]


def test_pattern_longer_than_text() -> None:
    assert rabin_karp("abcd", "abc") == []


def test_empty_pattern() -> None:
    assert rabin_karp("", "abc") == [0, 1, 2, 3]


def test_empty_text() -> None:
    assert rabin_karp("a", "") == []


def test_text_length_one() -> None:
    assert rabin_karp("a", "a") == [0]
    assert rabin_karp("b", "a") == []


# ------------------------------------------------------------
# 4. Чувствительность к регистру и спецсимволы
# ------------------------------------------------------------
def test_case_sensitive() -> None:
    assert rabin_karp("a", "A") == []
    assert rabin_karp("A", "A") == [0]


def test_case_difference_longer() -> None:
    assert rabin_karp("abc", "ABC") == []


def test_digits_and_symbols() -> None:
    assert rabin_karp("123", "012345") == [1]
    assert rabin_karp("!@#", "!!@#") == [1]


# ------------------------------------------------------------
# 5. Множественные вхождения
# ------------------------------------------------------------
def test_many_matches() -> None:
    text = "abc" * 100
    pattern = "abc"
    expected = list(range(0, len(text), 3))
    assert rabin_karp(pattern, text) == expected


def test_multiple_non_overlapping() -> None:
    assert rabin_karp("ab", "ab ab ab") == [0, 3, 6]


# ------------------------------------------------------------
# 6. Защита от коллизий (управляемые p и x)
# ------------------------------------------------------------
def test_collision_protection() -> None:
    # Без изменения p и x – пример, где коллизия возможна,
    # но посимвольная проверка отсекает ложное срабатывание
    text = "abcxabcdabxabcdabcdabcy"
    pattern = "abcdabcy"
    assert rabin_karp(pattern, text) == [15]


def test_collision_with_small_p_x() -> None:
    # Используем p=2, x=1: хеш строки = ord(c) % 2
    # 'a'(97) и 'c'(99) оба нечётные -> хеш 1, но строки разные
    assert rabin_karp("a", "c", p=2, x=1) == []
    # Та же ситуация с совпадающим символом – должно быть найдено
    assert rabin_karp("a", "a", p=2, x=1) == [0]

    # Дополнительно: p=3, x=2, символы 'a'(97%3=1) и 'd'(100%3=1)
    assert rabin_karp("a", "d", p=3, x=2) == []
    assert rabin_karp("a", "a", p=3, x=2) == [0]


# ------------------------------------------------------------
# 7. Случайные тесты (fuzzing)
# ------------------------------------------------------------
def naive_search(pattern: str, text: str) -> list[int]:
    result: list[int] = []
    m, n = len(pattern), len(text)
    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            result.append(i)  # noqa: PERF401
    return result


def test_random_small() -> None:
    for _ in range(100):
        text = "".join(random.choice(string.ascii_lowercase) for _ in range(50))
        pattern = "".join(random.choice(string.ascii_lowercase) for _ in range(5))
        assert rabin_karp(pattern, text) == naive_search(pattern, text)


# ------------------------------------------------------------
# 8. Стресс-тесты
# ------------------------------------------------------------
def test_large_input_short_pattern() -> None:
    text = "a" * 10000
    pattern = "aaa"
    expected = list(range(0, len(text) - len(pattern) + 1))
    assert rabin_karp(pattern, text) == expected


def test_large_input_long_pattern() -> None:
    text = "a" * 10000 + "b"
    pattern = "a" * 5000
    expected = list(range(0, 10001 - 5000))
    assert rabin_karp(pattern, text) == expected


# ------------------------------------------------------------
# 9. Одиночные символы и границы
# ------------------------------------------------------------
def test_single_char() -> None:
    assert rabin_karp("a", "bbbbba") == [5]


def test_all_same_chars() -> None:
    assert rabin_karp("aaa", "aaaaaa") == [0, 1, 2, 3]
