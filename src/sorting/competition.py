"""
Вы работаете в крупной компании, которая проводит ежегодный конкурс среди своих сотрудников.
В этом году было предложено решить сложную задачу, и все сотрудники, принявшие участие в конкурсе, получили
определенное количество баллов.

Ваша задача - определить медианное значение баллов. Медиана - это значение, которое делит упорядоченный набор данных
пополам, то есть половина всех значений меньше медианы, а другая половина - больше.

Формат ввода
На вход подается набор целых чисел, разделенных пробелами. Количество чисел в наборе не превосходит 1000.
Каждое число не превосходит 1000 по абсолютной величине.

Формат вывода
Выведите медианное значение баллов с точностью до шести знаков после запятой.

Пример
Вход:
5 2 3 4 1

Выход:
3.0
"""

from .quick_select import quick_select


def competition(scores: list[int]) -> float:
    """Решение задачи. Сложность O(N) в среднем."""
    n = len(scores)

    if n % 2 == 1:
        # Если количество элементов нечетное, возвращаем средний элемент
        return quick_select(scores, n // 2 + 1)
    else:
        # Если количество элементов четное, возвращаем среднее двух средних элементов
        left = quick_select(scores, n // 2)
        right = quick_select(scores, n // 2 + 1)

        return round((left + right) / 2, 6)
