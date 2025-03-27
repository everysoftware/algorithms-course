# O(n)
def divisors_naive(n: int) -> bool:
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return len(divisors) == 3


# O(sqrt(n))
def divisors_sqrt(n: int) -> bool:
    divisors_set = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors_set.add(i)
            divisors_set.add(n // i)
    divisors = sorted(divisors_set)
    return len(divisors) == 3


# O(sqrt(n))
def closest_divisors(n: int) -> list[int]:
    closest1 = two_closest(n + 1)
    closest2 = two_closest(n + 2)
    if closest1[1] - closest1[0] < closest2[1] - closest2[0]:
        result = closest1
    else:
        result = closest2
    return result


def two_closest(n: int) -> list[int]:
    lower, upper = [], []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lower.append(i)
            upper.append(n // i)
    return [lower[-1], upper[-1]]
