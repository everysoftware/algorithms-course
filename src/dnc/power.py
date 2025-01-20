# O(log n)
def fast_power(a: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        return fast_power(1 / a, -n)
    elif n % 2 == 1:
        return a * fast_power(a, n - 1)
    else:
        b = fast_power(a, n >> 1)
        return b * b
