"""
Слияние двух отсортированных массивов.

Даны два отсортированных массива A и B. Необходимо объединить их в один отсортированный массив C.

Формат ввода
В первой строке входных данных записано два числа N и M - длины массивов A и B соответственно (1 ≤ N, M ≤ 100000).
Во второй и третьей строках записаны массивы A и B соответственно. Элементы массивов - целые числа, по модулю не превосходящие 10^9.

Формат вывода
Нужно вывести элементы объединенного массива C в порядке неубывания.

Пример 1
Ввод
2 3
1 5
2 4 7
Вывод
1 2 4 5 7
"""


def merge(a: list[int], b: list[int]) -> list[int]:
    """
    Слияние двух отсортированных массивов. Сложность O(N + M).
    Принцип работы: проходим по обоим спискам и добавляем наименьший элемент в объединенный список.
    Если один из списков закончился, добавляем оставшиеся элементы другого списка.
    """
    n, m = len(a), len(b)
    res = []
    i = j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < n:
        res.append(a[i])
        i += 1

    while j < m:
        res.append(b[j])
        j += 1

    return res
