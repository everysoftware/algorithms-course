# O(n sqrt n)
def count_primes_sqrt(n: int) -> int:
    count = 0
    for i in range(2, n):
        if is_prime_sqrt(i):
            count += 1
    return count


# O(n * log(log(n)))
def count_primes_sieve(n: int) -> int:
    if n < 2:
        return 0
    # По условию задачи ищем простые числа строго меньшие n
    n -= 1
    numbers = [True] * (n + 1)
    numbers[0], numbers[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if numbers[i]:
            for j in range(i * i, n + 1, i):
                numbers[j] = False
    primes = [i for i in range(n + 1) if numbers[i]]
    return len(primes)


def is_prime_sqrt(n: int) -> bool:
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
