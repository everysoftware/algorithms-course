"""
Авторская задача.

В настольной игре “Манчкин” игроки сражаются с монстрами, используя различные карты. Каждая карта имеет свою силу
и стоимость. Цель игры - набрать наибольшее количество очков, победив монстров.

Представим, что у вас есть n карт, каждая из которых имеет определенную силу p[i] и стоимость c[i]. Ваша задача -
выбрать такой набор карт, чтобы суммарная сила была максимальной, но при этом суммарная стоимость не превышала ваш
бюджет B.

Теперь представим, что в игре есть m монстров, каждый из которых имеет определенную силу s[j]. Ваша задача - выбрать
такой набор карт, чтобы вы могли победить как можно больше монстров.
"""


def manchkin(
    budget: int, strength: list[int], gold: list[int], monster: list[int]
) -> int:
    n, m, k = len(strength), len(gold), len(monster)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            if gold[i - 1] <= j:
                dp[i][j] = max(
                    dp[i - 1][j], strength[i - 1] + dp[i - 1][j - gold[i - 1]]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    max_strength = dp[n][budget]
    monsters = 0
    for i in range(k):
        if monster[i] <= max_strength:
            monsters += 1

    return monsters
