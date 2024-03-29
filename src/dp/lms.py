"""
https://stepik.org/lesson/13257/step/5?unit=3442

Дан массив a из n целых чисел. Назовем подпоследовательностью длины k последовательность чисел
a[i1], a[i2], ..., a[ik], где 1 ≤ i1 < i2 < ... < ik ≤ n. Подпоследовательность называется кратной,
если каждый ее элемент делится на предыдущий. Например, последовательность 3, 6, 12 является кратной,
а последовательность 3, 6, 13 — нет.

Найдите длину самой длинной кратной подпоследовательности в массиве a.

Формат ввода
В первой строке вводится натуральное число n (1 <= n <= 1000) - количество элементов массива. Во второй
строке вводится n целых чисел, по модулю не превосходящих 10^9.

Формат вывода
Выведите наибольшую кратную подпоследовательность во входном массиве в том же порядке, в котором она
встречается в массиве. Если таких подпоследовательностей несколько, выведите ту, которая встречается раньше.

Пример:
Ввод
4
3 6 7 12
Вывод
3
"""


def lms(a: list[int]) -> int:
    """Нахождение длины самой длинной кратной подпоследовательности. Сложность O(N^2)"""
    n = len(a)
    length = [1] * n

    for i in range(n):
        for j in range(i):
            if a[i] % a[j] == 0 and length[j] + 1 > length[i]:
                length[i] = length[j] + 1

    return max(length)
