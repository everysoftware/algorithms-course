"""
Собеседование в Яндекс.

Даны две строки A и B. Необходимо определить, можно ли преобразовать строку A в строку B,
совершив не более одной операции вставки, удаления или замены символа.
"""


def can_transform(a: str, b: str) -> bool:
    """Решает задачу методом двух указателей. Сложность O(N)"""
    n, m = len(a), len(b)
    i, j = 0, 0
    diff_count = 0

    while i < n and j < m:
        if a[i] != b[j]:
            diff_count += 1

            if diff_count > 1:
                return False

            if n < m:
                j += 1
            elif n > m:
                i += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    # Если одна из строк закончилась, а другая нет, то нужно увеличить счетчик различий
    if i < n or j < m:
        diff_count += 1

    return diff_count <= 1
