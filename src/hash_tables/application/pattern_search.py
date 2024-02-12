X = 29
P = 999_999_000_001


def h(string):
    s = 0
    i = 0
    for i, c in enumerate(string):
        s += ord(c) * pow(X, i, P)
    s %= P
    return s, ord(string[-1]) * pow(X, i, P)


def pattern_search(pattern, text):
    """
    Находит все вхождения подстроки в текст
    :param pattern: подстрока
    :param text: текст
    :return: список позиций вхождения подстроки в текст
    """
    n, m = len(text), len(pattern)
    pattern_key = h(pattern)[0]
    prev_win = text[-m:]
    prev_win_key, prev_monom = h(prev_win)
    result = []

    i = -1
    p_pow = pow(X, m - 1, P)
    # идём с конца
    for i in range(-2, -(n - m) - 2, -1):
        if prev_win_key == pattern_key:
            result.append(n + i - m + 2)
        prev_win_key = ((prev_win_key - prev_monom) * X + ord(text[i - m + 1])) % P
        prev_monom = (ord(text[i]) * p_pow) % P
    else:
        if prev_win_key == pattern_key:
            result.append(n + i - m + 1)

    return result[::-1]


def pattern_search2(pattern, text):
    n, m = len(text), len(pattern)
    x, p = 59, 67  # взаимно простые
    # считаем заранее x^{0...m-1} mod p
    powers = [1]
    for i in range(1, m):
        powers.append((powers[-1] * x) % p)
    # хеш паттерна в обратную сторону
    # (чтобы считать ответ в прямом порядке)
    pattern_hash = sum((ord(pattern[i]) * powers[m - i - 1]) % p for i in range(m)) % p
    last_terms = [(ord(text[i]) * powers[-1]) % p for i in range(n - m + 1)]
    cur_hash = (
        last_terms[0] + sum((ord(text[i]) * powers[m - i - 1]) % p for i in range(1, m))
    ) % p
    result = []
    for i in range(n - m):
        if pattern_hash == cur_hash and pattern == text[i : i + m]:
            result.append(i)
        cur_hash = (((cur_hash - last_terms[i]) * x) % p + ord(text[i + m])) % p
    # последняя подстрока
    if pattern_hash == cur_hash and pattern == text[n - m :]:
        result.append(n - m)
    return result
