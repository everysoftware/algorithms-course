def fib_mod_two_last(n: int, m: int) -> int:
    """
    Остаток от деления числа Фибоначчи на m методом двух последних чисел. Сложность O(N).
    """
    fib1 = 0
    fib2 = 1

    for i in range(2, n + 1):
        fib1, fib2 = fib2, (fib1 + fib2) % m

    return fib2


def fib_mod_pisano(n: int, m: int) -> int:
    """Остаток от деления числа Фибоначчи на m по периоду Пизано. Сложность O(M)."""
    a = [0] * (6 * m + 2)
    a[1], a[2] = 1, 1

    i = 3
    while a[i - 1] != 1 or a[i - 2] != 0:
        a[i] = (a[i - 1] + a[i - 2]) % m
        i += 1

    # С i - 2 элемента последовательность повторяется. Значит, длина периода = i - 2.
    t = i - 2

    return a[n % t]
