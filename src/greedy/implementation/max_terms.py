def max_terms(n: int) -> list:
    result = []
    s = 0
    tmp = n
    for x in range(1, n + 1):
        n -= x
        if n >= x + 1:
            result.append(x)
            s += x
        else:
            result.append(tmp - s)
            break
    return result
