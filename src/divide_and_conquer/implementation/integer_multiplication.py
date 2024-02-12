"""
O(N^2)
y = {
    2*(y // 2), if y even
    1 + 2*(y // 2), if y odd
}
x * y = {
    2*(x * y // 2), if y even
    x + 2*(x * y // 2), if y odd
}
"""

"""
Возведение в степень работает за O(logN), где N - показатель степени.
Побитовые операции позволяют проводить операции 
над степенями двойки за O(1)
2^x = 1 << x
a * 2^x = a << x
a / 2^x = a >> x
Проверка чётности:
Если a чётное, то a & 1 = a & 0000 ... 0001 = 0
Если a нечётное, то a & 1 = 1
"""


def multiply_naive(x, y):
    if y == 0:
        return 0
    z = multiply_naive(x, y >> 1)
    if y & 1 == 0:
        return z << 1
    else:
        return x + (z << 1)


"""
Всё ещё O(N^2)
Разобъём числа на их левую и правую части: 
x = [x_l][x_r] = x_l * 2^(n // 2) + x_r
y = [y_l][y_r] = y_l * 2^(n // 2) + y_r
x * y = (x_l * 2^(n // 2) + x_r) * (y_l * 2^(n // 2) + y_r) =
= 2^n * (x_l * y_l) + 2^(n // 2) * ((x_l * y_r) + (x_r * y_l)) + (x_r * y_r)
Задача разделяется на 4 подзадачи.
"""


# длина числа
def length(x):
    if x <= 1:
        return 1
    result = 0
    while x > 0:
        x >>= 1
        result += 1
    return result


# получение правой и левой частей
def two_halves(x, n):
    half_n = n >> 1
    x_l = x >> half_n
    x_r = x & ((1 << half_n) - 1)
    return x_l, x_r


def multiply_intermediate(x, y):
    n = max(length(x), length(y))
    if n == 1:
        return x * y
    half_n = n >> 1
    x_l, x_r = two_halves(x, n)
    y_l, y_r = two_halves(y, n)
    # 2^n * (x_l * y_l) + 2^(n // 2) * ((x_l * y_r) + (x_r * y_l)) + (x_r * y_r)
    p1 = multiply_intermediate(x_l, y_l)
    p2 = multiply_intermediate(x_l, y_r)
    p3 = multiply_intermediate(x_r, y_l)
    p4 = multiply_intermediate(x_r, y_r)
    return (p1 << 2 * half_n) + ((p2 + p3) << half_n) + p4


"""
O(N^(log_2(3)) = O(N^1.6)
Вместо 4-ёх рек. вызовов будем делать 3:
(x_l * y_l), (x_r * y_r), (x_l + x_r) * (y_l + y_r)
Тогда:
(x_l * y_r + x_r * y_l) = (x_l + x_r)*(y_l + y_r) - (x_l * y_l) - (x_r * y_r)
"""


def karatsuba(x, y):
    n = max(length(x), length(y))
    if n == 1:
        return x * y
    half_n = n >> 1
    x_l, x_r = two_halves(x, n)
    y_l, y_r = two_halves(y, n)
    p1 = karatsuba(x_l, y_l)
    p2 = karatsuba(x_r, y_r)
    p3 = karatsuba(x_l + x_r, y_l + y_r)
    return (p1 << 2 * half_n) + ((p3 - p1 - p2) << half_n) + p2
