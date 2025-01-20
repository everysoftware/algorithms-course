# O(n^2), где n - количество бит в максимальном числе
import math


def multiply(x: str, y: str) -> str:
    return str(mul_karatsuba(int(x), int(y)))


# O(n^2), где n - количество бит в y
def mul_naive(x: int, y: int) -> int:
    """
    Принцип работы:
    y = {
        2 * (y // 2), если y - четное
        1 + 2 * (y // 2), если y - нечетное
    }
    x * y = {
        2 * (x * y // 2), если y - четное
        x + 2 * (x * y // 2), если y - нечетное
    }
    """
    if y == 0:
        return 0
    # Всего будет сделано n = log2(y) рекурсивных вызовов.
    # z = x * y // 2
    z = mul_naive(x, y >> 1)
    # Если y - четное, то x * y = 2 * (x * y // 2) = 2 * z
    if y & 1 == 0:
        return z << 1
    # Если y - нечетное, то x * y = x + 2 * (x * y // 2) = x + 2 * z
    else:
        return x + (z << 1)


# O(n^2), где n - количество бит в максимальном числе
def mul_dnc(x: int, y: int) -> int:
    """
    Принцип работы:
    Разобьём числа на левую и правую части:
    x = [x_l][x_r] = x_l * 2^(n // 2) + x_r
    y = [y_l][y_r] = y_l * 2^(n // 2) + y_r
    x * y = (x_l * 2^(n // 2) + x_r) * (y_l * 2^(n // 2) + y_r) =
    = 2^n * (x_l * y_l) + 2^(n // 2) * ((x_l * y_r) + (x_r * y_l)) + (x_r * y_r)

    Задача разделяется на 4 подзадачи:
    1) x_l * y_l
    2) x_l * y_r
    3) x_r * y_l
    4) x_r * y_r
    """
    n = max(bit_length(x), bit_length(y))
    if n <= 16:
        return x * y
    half_n = n >> 1
    x_l, x_r = two_halves(x, n)
    y_l, y_r = two_halves(y, n)
    # 2^n * (x_l * y_l) + 2^(n // 2) * ((x_l * y_r) + (x_r * y_l)) + (x_r * y_r)
    p1 = mul_dnc(x_l, y_l)
    p2 = mul_dnc(x_l, y_r)
    p3 = mul_dnc(x_r, y_l)
    p4 = mul_dnc(x_r, y_r)
    return (p1 << 2 * half_n) + ((p2 + p3) << half_n) + p4


# O(n^log2(3)) = O(n^1.6), где n - количество бит в максимальном числе
def mul_karatsuba(x: int, y: int) -> int:
    """
    Принцип работы:
    Вместо 4 рекурсивных вызовов будем делать 3 вызова:
    1) (x_l * y_l)
    2) (x_r * y_r)
    3) (x_l + x_r) * (y_l + y_r)

    Тогда слагаемое (x_l * y_r) + (x_r * y_l) можно выразить через слагаемые 1), 2) и 3):
    (x_l * y_r + x_r * y_l) = (x_l + x_r)*(y_l + y_r) - (x_l * y_l) - (x_r * y_r)
    """
    n = max(bit_length(x), bit_length(y))
    if n <= 16:
        return x * y
    x_l, x_r = two_halves(x, n)
    y_l, y_r = two_halves(y, n)
    p1 = mul_karatsuba(x_l, y_l)
    p2 = mul_karatsuba(x_r, y_r)
    p3 = mul_karatsuba(x_l + x_r, y_l + y_r)
    half_n = n >> 1
    return (p1 << 2 * half_n) + ((p3 - p1 - p2) << half_n) + p2


# O(n), где n - количество бит в числе
def bit_length(x: int) -> int:
    # Не делайте так.
    # if x <= 1:
    #     return 1
    # result = 0
    # while x > 0:
    #     x >>= 1
    #     result += 1
    # return result
    return math.ceil(math.log2(x + 1))


# O(n), где n - количество бит в числе
def two_halves(x: int, n: int) -> tuple[int, int]:
    half_n = n >> 1
    x_l = x >> half_n
    x_r = x & ((1 << half_n) - 1)
    return x_l, x_r
