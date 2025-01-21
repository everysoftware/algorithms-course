# O(n)
def primality_tests(n: int) -> tuple[list[int], int]:
    fermat_successful = 0
    miller_rabin_successful = [0, 0]
    d, s = decompose(n - 1)
    for a in range(1, n):
        # Тест Ферма
        if pow(a, n - 1, n) == 1:
            fermat_successful += 1
        # Проверяем первое условие Миллера-Рабина
        if pow(a, d, n) == 1:
            miller_rabin_successful[0] += 1
        # Проверяем второе условие Миллера-Рабина
        for r in range(s):
            if pow(a, (2**r) * d, n) == -1 % n:
                miller_rabin_successful[1] += 1
                break
    return miller_rabin_successful, fermat_successful


# O(log n)
def decompose(n: int) -> tuple[int, int]:
    s = 0
    while n % 2 == 0:
        n //= 2
        s += 1
    return n, s
