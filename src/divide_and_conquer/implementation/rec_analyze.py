from math import log


def rec_analyze(x):
    a, b, d = x
    n = int(10e100)
    log_ab = log(a, b)
    if d > log_ab:
        return n**d
    elif d == log_ab:
        return n**d * log(n)
    else:
        return n**log_ab


def rec_analyze_str(x):
    a, b, d = x
    n = int(10e100)
    log_ab = log(a, b)
    if d > log_ab:
        return f"n^{d}"
    elif d == log_ab:
        return f"n^{d}log(n)"
    else:
        return f"n^log_{b}({a})"
