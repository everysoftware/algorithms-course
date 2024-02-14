"""
Дана последовательность N целых чисел и M запросов.

Каждый запрос представляет собой пару целых чисел L_i и R_i (1 <= L_i <= R_i <= N). Для каждого запроса
вывести количество нулей на полуинтервале последовательности [L, R).

Пример:
a = [1, 0, 0, 1, 0, 1, 0, 1]
requests = [(0, 3), (1, 5), (2, 7)]

Ответ: [2, 3, 3]
"""


def count_zero(a: list[int], requests: list[tuple[int, int]]) -> list[int]:
    """Префиксные суммы. Сложность O(N + M)."""
    n = len(a)

    # Подсчитываем префиксные суммы
    prefix_sum = [0] * (n + 1)
    """prefix_sum[i] - количество нулей на префиксе длины i."""
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (a[i - 1] == 0)

    # Подсчитываем ответы на запросы
    answers = []
    for left, right in requests:
        answers.append(prefix_sum[right] - prefix_sum[left])

    return answers
