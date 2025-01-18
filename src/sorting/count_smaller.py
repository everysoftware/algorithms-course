import bisect
import math
from collections import deque


# O(n^2)
def count_smaller_bisect(nums: list[int]) -> list[int]:
    sorted_list: list[int] = []
    result: list[int] = []
    # Находим индекс, куда можно вставить num
    for num in reversed(nums):
        position = bisect.bisect_left(sorted_list, num)
        result.append(position)
        # Вставляем num в отсортированный список
        sorted_list.insert(position, num)
    # Переворачиваем результат, чтобы получить правильный порядок
    return result[::-1]


Item = tuple[int, int]


# O(n)
def count(a: list[Item], b: list[Item], counts: list[int]) -> list[Item]:
    n, m = len(a), len(b)
    res = []
    i = j = 0
    inversions = 0
    while i < n and j < m:
        if a[i][0] <= b[j][0]:
            res.append(a[i])
            counts[a[i][1]] += inversions
            i += 1
        else:
            res.append(b[j])
            inversions += 1
            j += 1
    while i < n:
        res.append(a[i])
        counts[a[i][1]] += inversions
        i += 1
    while j < m:
        res.append(b[j])
        j += 1
    return res


# O(n log n)
def count_smaller_merge(a: list[int]) -> list[int]:
    # Добиваем кол-во элементов до степени двойки
    n = len(a)
    diff = 0
    while not math.log2(n + diff).is_integer():
        diff += 1
    a = [0] * diff + a
    q: deque[list[Item]] = deque([[(x, i)] for i, x in enumerate(a)])
    counts = [0] * (n + diff)
    while len(q) > 1:
        left = q.popleft()
        right = q.popleft()
        result = count(left, right, counts)
        q.append(result)
    return counts[diff:]
