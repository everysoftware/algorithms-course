"""
Дана последовательность из N натуральных чисел. Рассматриваются все её непрерывные подпоследовательности длиной
не менее пяти элементов, такие что сумма элементов каждой из них кратна k. Найдите количество таких
подпоследовательностей.

Входные данные
Даны два входных файла (файл A и файл B), каждый из которых содержит в первой строке делитель k
(1 <= k <= 10000) и количество чисел N (1 ≤ N ≤ 10 000 000). Каждая из следующих N строк содержит одно
натуральное число, не превышающее 10 000.

Пример организации исходных данных во входном файле:
117 9
108
129
143
186
72
195
94
38
69


В данной последовательности условиям удовлетворяют подпоследовательности
129, 143, 186, 72, 195, 94;
186, 72, 195, 94, 38;
72, 195, 94, 38, 69

Поэтому ответ для приведённого примера 3

В ответе укажите два числа: сначала значение искомой суммы для файла А, затем – для файла B.
"""

from collections import deque


def count_subsequence_naive(k: int, a: list[int]) -> int:
    """Перебор всех подпоследовательностей. Сложность O(N^2)"""
    n = len(a)
    count = 0

    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s % k == 0 and j - i + 1 >= 5:
                count += 1

    return count


def count_subsequence_ps(k: int, a: list[int]) -> int:
    """Префиксные суммы. Сложность O(N)."""
    n = len(a)
    tails = [0] * k
    count = 0
    s = 0

    # Заполняем очередь первыми 4-мя префиксными суммами первых
    queue = deque()
    for i in range(4):
        s += a[i]
        queue.append(s)

    # Подсчитываем количество подпоследовательностей
    for i in range(4, n):
        # Добавляем новый элемент в сумму
        s += a[i]

        # Обновляем количество подпоследовательностей
        if s % k == 0:
            count += 1

        # Со всеми хвостами того же остатка, что и s можно составить новую подпоследовательность
        count += tails[s % k]

        # Обновляем число хвостов с остатком первой префиксной суммы в очереди. Теперь её можно использовать для
        # составления новых подпоследовательностей, так как она находится на расстоянии не менее 5 элементов
        # для всех будущих элементов.
        tails[queue.popleft() % k] += 1

        # Добавляем префиксную сумму в очередь
        queue.append(s)

    return count