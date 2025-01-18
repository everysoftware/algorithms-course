# O(n + m)
def sales_sum(sales: list[int], queries: list[tuple[int, int]]) -> list[int]:
    n = len(sales)
    # Пусть p[i] - общая сумма продаж за первые i дней.
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = p[i - 1] + sales[i - 1]
    # Подсчитываем ответы на запросы
    answers = []
    for start_day, end_day in queries:
        # Стартовый день включается, поэтому данные за него мы не вычитаем.
        answers.append(p[end_day] - p[start_day - 1])
    return answers
