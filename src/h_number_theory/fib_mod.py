# O(n)
def fib_mod_two_last(n: int, m: int) -> int:
    fib1 = 0
    fib2 = 1
    for _ in range(2, n + 1):
        fib1, fib2 = fib2, (fib1 + fib2) % m
    return fib2


# O(m)
def fib_mod_pisano(n: int, m: int) -> int:
    a = [0] * (6 * m + 2)
    a[1], a[2] = 1, 1
    i = 3
    while a[i - 1] != 1 or a[i - 2] != 0:
        a[i] = (a[i - 1] + a[i - 2]) % m
        i += 1
    # С i - 2 элемента последовательность повторяется. Значит, длина периода = i - 2.
    t = i - 2
    return a[n % t]
