from collections import deque


# O(n^2)
def count_subsequences_naive(k: int, a: list[int]) -> int:
    n = len(a)
    count = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s % k == 0 and j - i + 1 >= 5:
                count += 1
    return count


# O(n)
def count_subsequences_ps(k: int, a: list[int]) -> int:
    n = len(a)
    # prefix_count[i] - количество префиксов с остатком i
    prefix_count = [0] * k
    count, s = 0, 0
    # Заполняем очередь первыми 4 префиксами
    queue: deque[int] = deque()
    for i in range(4):
        s += a[i]
        queue.append(s)
    # Подсчитываем ответ
    for i in range(4, n):
        # Добавляем новый элемент в сумму, теперь в подпоследовательности не менее 5 элементов
        s += a[i]
        # Обновляем количество подходящих подпоследовательностей
        if s % k == 0:
            count += 1
        # Со всеми префиксами того же остатка, что и S можно составить новую подпоследовательность
        count += prefix_count[s % k]
        # Обрабатываем первый префикс в очереди: теперь его можно использовать для составления новых
        # подпоследовательностей.
        prefix_count[queue.popleft() % k] += 1
        # Кладем текущий префикс в очередь
        queue.append(s)
    return count
