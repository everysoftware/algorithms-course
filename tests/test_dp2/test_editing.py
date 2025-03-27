from collections.abc import Callable

import pytest

from src.l_dp2.edit_candidates import edit_candidates
from src.l_dp2.edit_distance import (
    edit_distance_dp,
    edit_distance_rec,
)
from src.l_dp2.edit_path import Operation, PathItem, edit_path


@pytest.mark.parametrize("func", [edit_distance_rec, edit_distance_dp])
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
def test_edit_distance_dp(func: Callable[[str, str], int], a: str, b: str, expected: int) -> None:
    assert func(a, b) == expected


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
def test_editing(a: str, words: list[str], expected: tuple[int, list[str]]) -> None:
    assert edit_candidates(a, words) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (
            "sitting",
            "kitten",
            (
                3,
                [
                    PathItem(Operation.REPLACE, 0, ("s", "k")),
                    PathItem(Operation.MATCH, 1, ("i",)),
                    PathItem(Operation.MATCH, 2, ("t",)),
                    PathItem(Operation.MATCH, 3, ("t",)),
                    PathItem(Operation.REPLACE, 4, ("i", "e")),
                    PathItem(Operation.MATCH, 5, ("n",)),
                    PathItem(Operation.DELETE, 6, ("g",)),
                ],
            ),
        ),
        (
            "autozavod",
            "pivzavod",
            (
                4,
                [
                    PathItem(Operation.DELETE, 0, ("a",)),
                    PathItem(Operation.REPLACE, 1, ("u", "p")),
                    PathItem(Operation.REPLACE, 2, ("t", "i")),
                    PathItem(Operation.REPLACE, 3, ("o", "v")),
                    PathItem(Operation.MATCH, 4, ("z",)),
                    PathItem(Operation.MATCH, 5, ("a",)),
                    PathItem(Operation.MATCH, 6, ("v",)),
                    PathItem(Operation.MATCH, 7, ("o",)),
                    PathItem(Operation.MATCH, 8, ("d",)),
                ],
            ),
        ),
        (
            "sunday",
            "saturday",
            (
                3,
                [
                    PathItem(Operation.MATCH, 0, ("s",)),
                    PathItem(Operation.INSERT, 1, ("a",)),
                    PathItem(Operation.INSERT, 1, ("t",)),
                    PathItem(Operation.MATCH, 1, ("u",)),
                    PathItem(Operation.REPLACE, 2, ("n", "r")),
                    PathItem(Operation.MATCH, 3, ("d",)),
                    PathItem(Operation.MATCH, 4, ("a",)),
                    PathItem(Operation.MATCH, 5, ("y",)),
                ],
            ),
        ),
        ("", "", (0, [])),
        ("a", "", (1, [PathItem(Operation.DELETE, 0, ("a",))])),
        ("", "a", (1, [PathItem(Operation.INSERT, 0, ("a",))])),
        ("a", "a", (0, [PathItem(Operation.MATCH, 0, ("a",))])),
    ],
)
def test_edit_path(a: str, b: str, expected: list[PathItem]) -> None:
    assert edit_path(a, b) == expected
