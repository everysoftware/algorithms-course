INITIAL_P = 1_000_000_007
INITIAL_X = 263


def rabin_karp(pattern: str, text: str, p: int = INITIAL_P, x: int = INITIAL_X) -> list[int]:
    n, m = len(text), len(pattern)

    if m > n:
        return []

    # precompute x^(m-1) % p
    x_pow = pow(x, m - 1, p)

    # hash pattern
    pattern_hash = 0
    for c in pattern:
        pattern_hash = (pattern_hash * x + ord(c)) % p

    # hash first window
    window_hash = 0
    for i in range(m):
        window_hash = (window_hash * x + ord(text[i])) % p

    result = []

    for i in range(n - m + 1):
        # проверка совпадения
        if window_hash == pattern_hash and text[i : i + m] == pattern:  # защита от коллизий
            result.append(i)

        # rolling hash
        if i < n - m:
            window_hash = ((window_hash - ord(text[i]) * x_pow) * x + ord(text[i + m])) % p

    return result
