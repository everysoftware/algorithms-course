from collections import deque


# O(n^2)
def sliding_window_naive(n: int, a: list[int], m: int) -> list[int]:
    result = []
    for i in range(n - m + 1):
        result.append(max(a[i : i + m]))
    return result


# O(n)
def sliding_window_deque(n: int, a: list[int], m: int) -> list[int]:
    d: deque[int] = deque()
    # Заполняем очередь для первого окна
    for i in range(m):
        # Удаляем элементы из окна, которые <= текущего
        while d and a[d[-1]] <= a[i]:
            d.pop()
        d.append(i)
    # Обрабатываем остальные окна
    result = []
    for i in range(m, n):
        # Добавляем максимум текущего окна
        result.append(a[d[0]])
        # Удаляем элементы, которые вышли из окна
        while d and d[0] <= i - m:
            d.popleft()
        # Удаляем элементы из окна, которые <= текущего
        while d and a[d[-1]] <= a[i]:
            d.pop()
        d.append(i)
    last_max = a[d.popleft()]
    result.append(last_max)
    return result
