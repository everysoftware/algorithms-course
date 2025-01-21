from collections import deque


# O(n^2)
def sliding_window_naive(n: int, a: list[int], m: int) -> list[int]:
    result = []
    # Проходим по всем окнам и находим максимум в каждом
    for i in range(n - m + 1):
        window = a[i : i + m]
        result.append(max(window))
    return result


# O(n)
def sliding_window_deque(n: int, a: list[int], m: int) -> list[int]:
    q: deque[int] = deque()
    result = []
    for i, num in enumerate(a):
        # Удаляем элемент, вышедший из окна
        if i >= m and a[i - m] == q[0]:
            q.popleft()
        # Удаляем элементы, меньшие текущего
        while q and q[-1] < num:
            q.pop()
        # Добавляем текущий элемент в очередь
        q.append(num)
        # Добавляем максимум окна
        if i + 1 >= m:
            result.append(q[0])
    return result
