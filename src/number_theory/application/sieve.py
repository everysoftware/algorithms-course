"""
https://contest.yandex.ru/contest/29847/problems/B/

Решето Эратосфена
"""


def sieve(n: int) -> list[int]:
    """Решето Эратосфена. Поиск всех простых чисел до N. Сложность O(Nlog(log(N)))."""
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]
