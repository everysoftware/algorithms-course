from typing import Callable

import pytest

from src.dp2 import (
    ed_dp,
    ed_rec,
    edit_path,
    EditOperation,
    editing,
)


@pytest.mark.parametrize("func", [ed_rec, ed_dp])
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("kitten", "sitting", 3),
        ("autozavod", "pivzavod", 4),
        ("sunday", "saturday", 3),
        ("", "", 0),
        ("a", "", 1),
        ("", "a", 1),
        ("a", "a", 0),
    ],
)
def test_edit_distance_dp(func: Callable[[str, str], int], a: str, b: str, expected: int):
    assert func(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (
            "sitting",
            "kitten",
            (
                3,
                [
                    (EditOperation.REPLACE, 1, "s", "k"),
                    (EditOperation.REPLACE, 5, "i", "e"),
                    (EditOperation.DELETE, 7, "g", -1),
                ],
            ),
        ),
        (
            "autozavod",
            "pivzavod",
            (
                4,
                [
                    (EditOperation.DELETE, 1, "a", -1),
                    (EditOperation.REPLACE, 2, "u", "p"),
                    (EditOperation.REPLACE, 3, "t", "i"),
                    (EditOperation.REPLACE, 4, "o", "v"),
                ],
            ),
        ),
        (
            "sunday",
            "saturday",
            (
                3,
                [
                    (EditOperation.INSERT, 2, "a", -1),
                    (EditOperation.INSERT, 2, "t", -1),
                    (EditOperation.REPLACE, 3, "n", "r"),
                ],
            ),
        ),
        ("", "", (0, [])),
        ("a", "", (1, [(EditOperation.DELETE, 1, "a", -1)])),
        ("", "a", (1, [(EditOperation.INSERT, 1, "a", -1)])),
        ("a", "a", (0, [])),
    ],
)
def test_edit_path(a: str, b: str, expected: list):
    assert edit_path(a, b) == expected


@pytest.mark.parametrize(
    "a, words, expected",
    [
        # Пример из задания
        (
            "whiskbroom",
            [
                "congratulatory",
                "frissell",
                "carpers",
                "scatters",
                "almuerzo",
                "igneous",
                "screenage",
                "polderboy",
                "studentship",
            ],
            (8, ["frissell", "almuerzo", "igneous", "polderboy"]),
        ),
        # Одинаковые слова
        ("whiskbroom", ["whisk", "broom", "whiskbroom"], (0, ["whiskbroom"])),
        # Одно слово
        ("kitten", ["sitting"], (3, ["sitting"])),
        # Несколько слов
        ("kitten", ["sitting", "kitchen", "kit"], (2, ["kitchen"])),
        # Одинаковое минимальное расстояние
        ("kitten", ["sitting", "kitchen", "mitten"], (1, ["mitten"])),
        # Пустая строка
        ("", ["sitting", "kitchen", "mitten"], (6, ["mitten"])),
    ],
)
def test_editing(a: str, words: list[str], expected: tuple[int, list[str]]):
    assert editing(a, words) == expected
