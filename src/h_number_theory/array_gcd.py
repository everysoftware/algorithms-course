def find_gcd(nums: list[int]) -> int:
    return gcd_euclid(min(nums), max(nums))


# O(min(a, b))
def gcd_naive(a: int, b: int) -> int:
    res = 1
    for d in range(2, min(a, b)):
        if a % d == 0 and b % d == 0:
            res = d
    return res


# O(log(min(a, b)))
def gcd_euclid(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# O(log(min(a, b)))
def gcd_euclid_rec(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd_euclid_rec(b, a % b)
