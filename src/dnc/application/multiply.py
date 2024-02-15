"""Быстрое умножение целых чисел."""


def multiply_naive(x: int, y: int) -> int:
    """
    Умножение двух больших чисел методом "в лоб". Сложность O(N^2), где N - количество бит в числе.

    Принцип работы:
    y = {
        2 * (y // 2), если y четный
        1 + 2 * (y // 2), если y нечетный
    }
    x * y = {
        2 * (x * y // 2), если y четный
        x + 2 * (x * y // 2), если y нечетный
    }
    """
    if y == 0:
        return 0

    # Всего будет сделано N = log2(y) рекурсивных вызовов.
    z = multiply_naive(x, y >> 1)

    # На каждом вызове будет сделано O(1) операций, если мы имеем дело с небольшими числами, потому что
    # используются побитовые операции. Однако, если мы имеем дело с большими числами, которые представляются
    # строками, то на каждом вызове будет
    # сделано O(N) операций.
    if y & 1 == 0:
        return z << 1
    else:
        return x + (z << 1)


def length(x: int) -> int:
    """Длина числа в двоичной системе счисления. Сложность O(log(X))."""
    if x <= 1:
        return 1

    result = 0
    while x > 0:
        x >>= 1
        result += 1

    return result


def two_halves(x: int, n: int) -> tuple[int, int]:
    """Получение левой и правой частей числа. Сложность O(1)."""
    half_n = n >> 1
    x_l = x >> half_n
    x_r = x & ((1 << half_n) - 1)

    return x_l, x_r


def multiply_dnc(x: int, y: int) -> int:
    """
    Умножение двух больших чисел методом разделяй и властвуй. Сложность всё ещё O(N^2), где N - количество бит
    в числе.

    Принцип работы:
    Разобьём числа на их левую и правую части:
    x = [x_l][x_r] = x_l * 2^(n // 2) + x_r
    y = [y_l][y_r] = y_l * 2^(n // 2) + y_r
    x * y = (x_l * 2^(n // 2) + x_r) * (y_l * 2^(n // 2) + y_r) =
    = 2^n * (x_l * y_l) + 2^(n // 2) * ((x_l * y_r) + (x_r * y_l)) + (x_r * y_r)

    Таким образом, задача разделяется на 4 подзадачи:
    1) x_l * y_l
    2) x_l * y_r
    3) x_r * y_l
    4) x_r * y_r
    """

    n = max(length(x), length(y))

    if n <= 16:
        return x * y

    half_n = n >> 1
    x_l, x_r = two_halves(x, n)
    y_l, y_r = two_halves(y, n)

    # 2^n * (x_l * y_l) + 2^(n // 2) * ((x_l * y_r) + (x_r * y_l)) + (x_r * y_r)
    p1 = multiply_dnc(x_l, y_l)
    p2 = multiply_dnc(x_l, y_r)
    p3 = multiply_dnc(x_r, y_l)
    p4 = multiply_dnc(x_r, y_r)

    return (p1 << 2 * half_n) + ((p2 + p3) << half_n) + p4


def karatsuba(x: int, y: int) -> int:
    """
    Умножение двух больших чисел методом Карацубы. Сложность O(N^log2(3)) = O(N^1.6), где N - количество
    бит в числе.

    Принцип работы:
    Вместо 4 рекурсивных вызовов будем делать 3 вызова:
    1) (x_l * y_l)
    2) (x_r * y_r)
    3) (x_l + x_r) * (y_l + y_r)
    Тогда слагаемое (x_l * y_r) + (x_r * y_l) можно выразить через слагаемые 1), 2) и 3):
    (x_l * y_r + x_r * y_l) = (x_l + x_r)*(y_l + y_r) - (x_l * y_l) - (x_r * y_r)
    """
    n = max(length(x), length(y))

    if n <= 16:
        return x * y

    x_l, x_r = two_halves(x, n)
    y_l, y_r = two_halves(y, n)
    p1 = karatsuba(x_l, y_l)
    p2 = karatsuba(x_r, y_r)
    p3 = karatsuba(x_l + x_r, y_l + y_r)

    half_n = n >> 1

    return (p1 << 2 * half_n) + ((p3 - p1 - p2) << half_n) + p2
