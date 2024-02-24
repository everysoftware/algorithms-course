"""
https://stepik.org/lesson/13248/step/5

Первая строка содержит число 1 ≤ n ≤ 10^5, вторая — массив A[1…n], содержащий натуральные числа,
не превосходящие 10^9. Необходимо посчитать число пар индексов 1 ≤ i < j ≤ n, для которых A[i] > A[j].
(Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором
смысле его «отсортированностью»: чем меньше инверсий, тем ближе массив к отсортированному виду.)

Пример
Вход:
5
2 3 9 2 9
Выход:
2
Пояснение:
В данном массиве две инверсии: (2, 2) и (3, 2).
"""

import math
from collections import deque


def merge_and_count(a: list[int], b: list[int]) -> tuple[list[int], int]:
    """Слияние двух отсортированных списков и подсчёт инверсий. Сложность O(N)."""
    n, m = len(a), len(b)
    res = []
    i = j = 0
    inv_count = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

            # Если элемент из второго списка меньше, чем элемент из первого списка,
            # то он образует инверсию с оставшимися элементами первого списка.
            if i < n:
                inv_count += n - i

    while i < n:
        res.append(a[i])
        i += 1

    while j < m:
        res.append(b[j])
        j += 1

    return res, inv_count


def count_inverse(a: list[int]) -> int:
    n = len(a)
    queue = deque()

    # Добиваем кол-во элементов до степени двойки
    while not math.log2(n).is_integer():
        queue.append([0])
        n += 1

    # Добавляем элементы в очередь
    for x in a:
        queue.append([x])

    count = 0
    while len(queue) > 1:
        merged, inv_count = merge_and_count(queue.popleft(), queue.popleft())
        queue.append(merged)
        count += inv_count

    return count
