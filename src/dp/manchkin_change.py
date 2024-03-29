"""
Авторская задача (И. Стасевич).

Вы - отважный Манчкин, исследующий подземелья в поисках сокровищ. Ваша цель - собрать определенное количество
золота (N), используя монеты, которые вы нашли в подземелье. Монеты имеют номиналы 1, 3, 5 и 10.

Однако есть одно условие: вы хотите минимизировать вес золота, которое вы несете. Поэтому вам нужно найти способ
собрать требуемую сумму, используя наименьшее количество монет.

Ваша задача - определить, сколько монет вам понадобится, чтобы достичь вашей цели. Удачи, Манчкин!

Формат ввода
На вход подается одно целое число N (1 ≤ N ≤ 10^5) - количество золота, которое вы хотите собрать.

Формат вывода
Выведите одно целое число - минимальное количество монет, которое вам понадобится, чтобы собрать N золота.

Пример
Ввод
11
Вывод
2

Эта задача эквивалентна задаче о рюкзаке с повторениями.
"""

INF = 10**20


def manchkin_change(n: int) -> int:
    """Решение задачи. Возвращает минимальное количество монет для сбора суммы n. Сложность O(N)."""
    coins = [1, 3, 5, 10]
    min_coins = [INF] * (n + 1)
    """min_coins[i] - минимальное количество монет для сбора суммы i"""
    min_coins[0] = 0

    for i in range(1, n + 1):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[n]
