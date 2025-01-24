"""
Авторская задача (М. Покровский).
https://leetcode.com/problems/longest-common-subsequence/description/
https://leetcode.com/problems/shortest-common-supersequence/
https://leetcode.com/problems/longest-palindromic-subsequence/

Ваня и Вова собирают конструктор лего. Каждый из них строит свою башню из кубиков различных цветов. Построив башню,
они хотят найти наибольшую общую последовательность цветов между своими башнями. Помогите им это сделать.

Формат ввода.
В первой строке записаны два числа n и m (1 ≤ n, m ≤ 1000) — количество кубиков в башнях Вани и Вовы соответственно.
В следующей строке записаны n целых чисел a1, a2, ..., an (1 ≤ ai ≤ 1000) — цвета кубиков в башне Вани.

Формат вывода.
Выведите наибольшую общую последовательность цветов кубиков. Если таких последовательностей несколько, выведите
первую найденную.

Пример
Ввод
3 3
1 2 3 2 1
3 2 1 4 7
Вывод
3 2 1
"""


def towers(tower1: list[int], tower2: list[int]) -> list[int]:
    n, m = len(tower1), len(tower2)

    # Создаем таблицу для хранения длин LSS
    length = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Максимальная длина LSS
    max_len = 0
    # Координаты конца LSS
    end_pos = 0

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Если цвета совпадают, то длина LSS увеличивается на 1
            if tower1[i - 1] == tower2[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1

                if length[i][j] > max_len:
                    max_len = length[i][j]
                    end_pos = i - 1
            # Если цвета не совпадают, то длина LSS равна 0
            else:
                length[i][j] = 0

    # Восстанавливаем LSS
    path = tower1[end_pos - max_len + 1 : end_pos + 1]

    return path
