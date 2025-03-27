from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any

from src.l_dp2.edit_distance import get_dp_table


class Operation(StrEnum):
    MATCH = auto()
    DELETE = auto()
    INSERT = auto()
    REPLACE = auto()


@dataclass(frozen=True)
class PathItem:
    op: Operation
    at: int
    args: Iterable[Any]


# O(n * m)
def edit_path(a: str, b: str) -> tuple[int, list[PathItem]]:
    n, m = len(a), len(b)
    distance = get_dp_table(a, b)
    return distance[n][m], get_path(n, m, a, b, distance)


# O(n + m)
def get_path(n: int, m: int, a: str, b: str, dp: list[list[int]]) -> list[PathItem]:
    path: list[PathItem] = []
    i, j = n, m
    while i > 0 and j > 0:
        # Совпадение
        if a[i - 1] == b[j - 1]:
            path.append(PathItem(op=Operation.MATCH, at=i - 1, args=(a[i - 1],)))
            i -= 1
            j -= 1
        else:
            # Замена
            if dp[i][j] == dp[i - 1][j - 1] + 1:
                path.append(PathItem(op=Operation.REPLACE, at=i - 1, args=(a[i - 1], b[j - 1])))
                i -= 1
                j -= 1
            # Вставка
            elif dp[i][j] == dp[i][j - 1] + 1:
                path.append(PathItem(op=Operation.INSERT, at=i, args=(b[j - 1],)))
                j -= 1
            # Удаление
            else:
                path.append(PathItem(op=Operation.DELETE, at=i - 1, args=(a[i - 1],)))
                i -= 1
    # Если осталась строка A, удаляем лишние символы
    while i > 0:
        path.append(PathItem(op=Operation.DELETE, at=i - 1, args=(a[i - 1],)))
        i -= 1
    # Если осталась строка B, вставляем недостающие символы
    while j > 0:
        path.append(PathItem(op=Operation.INSERT, at=0, args=(b[j - 1],)))
        j -= 1
    return path[::-1]
