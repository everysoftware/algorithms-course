"""
Авторская задача (И. Стасевич)

Представьте, что вы работаете в большой компании, и у вас есть список из N задач, которые нужно выполнить.
Каждая задача имеет статус, представленный целым числом:

- 0 означает, что задача не выполнена
- 1 означает, что задача в процессе
- 2 означает, что задача выполнена

Ваш менеджер часто просит вас предоставить отчёт о количестве невыполненных задач в определённых интервалах.
Например, менеджер может попросить вас подсчитать количество невыполненных задач с 1-й по 3-ю, с 2-й по 5-ю или
с 3-й по 7-ю.

Ваша задача - написать программу, которая быстро обрабатывает эти запросы и возвращает количество невыполненных
задач для каждого интервала. Это поможет вам сэкономить время и сделать вашу работу более эффективной.

Формат ввода:
Первая строка содержит два целых числа N и M (1 <= N, M <= 10^5) - количество задач и количество запросов.
Вторая строка содержит N целых чисел - статусы задач, разделенные пробелами.
Следующие M строк содержат запросы, каждый запрос представляет собой пару целых чисел L_i и R_i (1 <= L_i <= N,
L_i <= R_i <= N).

Формат вывода:
Для каждого запроса выведите количество невыполненных задач.

Пример:
Ввод:
8 3
1 0 0 1 0 1 0 1
1 3
2 5
3 7

Вывод:
2 3 3
"""


def unfinished_tasks(a: list[int], requests: list[tuple[int, int]]) -> list[int]:
    """Префиксные суммы. Сложность O(N + M)."""
    n = len(a)

    # Подсчитываем префиксные суммы
    prefix_sum = [0] * (n + 1)
    """prefix_sum[i] - количество нулей на первых i элементах [1, i]."""
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (a[i - 1] == 0)

    # Подсчитываем ответы на запросы
    answers = []
    for left, right in requests:
        # Стартовый день включается, поэтому данные за него мы не вычитаем.
        answers.append(prefix_sum[right] - prefix_sum[left - 1])

    return answers