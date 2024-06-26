"""
Авторская задача (И. Стасевич).

В настольной игре “Манчкин” игроки сражаются с монстрами, используя различные шмотки. Каждая шмотка имеет свою силу
и стоимость. Цель игры - набрать наибольшее количество очков, победив монстров.

Представим, что у вас есть N шмоток, каждая из которых имеет определенную силу p[i] и стоимость c[i].
В игре также есть M монстров, каждый из которых имеет определенную силу s[j]. Необходимо
выбрать такой набор шмоток, чтобы их суммарная сила была максимальной, но при этом суммарная стоимость не превышала ваш
бюджет B. В качестве ответа необходимо вывести количество монстров, которых вы сможете победить с выбранным набором
шмоток (бой с каждым монстром происходит по отдельности).

Формат ввода.
В первой строке входных данных содержатся три числа: N, M и B (1 ≤ N, M ≤ 100, 1 ≤ B ≤ 1000) - количество карт,
количество монстров и ваш бюджет. В следующей строке содержатся N чисел p[i] (1 ≤ p[i] ≤ 100) - силы карт.
В следующей строке содержатся N чисел c[i] (1 ≤ c[i] ≤ 100) - стоимость карт. В последней строке содержатся M
чисел s[j] (1 ≤ s[j] ≤ 100) - силы монстров.

Формат вывода.
Выведите одно число - количество монстров, которых вы сможете победить.

Пример
Ввод
3 3 10
1 2 3
1 2 3
1 2 3
Вывод
3
"""


def max_score(
    budget: int, strength: list[int], gold: list[int], monster: list[int]
) -> int:
    n, k = len(strength), len(monster)
    max_strength = [0 for _ in range(budget + 1)]
    """max_strength[i] - максимальная сила, которую можно получить, потратив i золота."""

    for i in range(n):
        item_cost, item_strength = gold[i], strength[i]
        for j in range(budget, item_cost - 1, -1):
            max_strength[j] = max(
                max_strength[j], item_strength + max_strength[j - item_cost]
            )

    manchkin_strength = max_strength[budget]
    monsters = 0
    for i in range(k):
        if manchkin_strength > monster[i]:
            monsters += 1

    return monsters
