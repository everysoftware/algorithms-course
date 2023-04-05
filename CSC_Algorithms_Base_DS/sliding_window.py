from collections import deque


"""
Найти максимум в каждом окне размера m данного массива чисел
A[1 . . . n].
"""


# O(N*M)
def sliding_window_naive(n, a, m):
    result = []
    for i in range(n - m + 1):
        result.append(max(a[i:i + m]))
    return result


# O(N)
def sliding_window(n, a, m):
    q = deque()
    for i in range(m):
        # чистим элементы меньшие или равные текущему
        while q and a[i] >= a[q[-1]]:
            q.pop()
        # добавляем текущий
        q.append(i)
    result = []
    for i in range(m, n):
        result.append(a[q[0]])
        # удаляем вышедшие из окна элементы
        while q and q[0] <= i - m:
            q.popleft()
        # удаляем элементы, меньшие текущего
        while q and a[i] >= a[q[-1]]:
            q.pop()
        q.append(i)
    result.append(a[q[0]])
    return result
