from introduction.tasks import calculate, fib_two_last, fib_mod_pisano, gcd_euclid


def solve_fib() -> None:
    n = int(input())
    print(fib_two_last(n))


def solve_fib_last_digit() -> None:
    n = int(input())
    print(fib_mod_pisano(n, 10))


def solve_fib_mod() -> None:
    n, m = map(int, input().split())
    print(fib_mod_pisano(n, m))


def solve_gcd() -> None:
    a, b = list(map(int, input().split()))
    print(gcd_euclid(a, b))


def solve_bigo() -> None:
    print(
        "It is not the answer to the Ultimate Question of Life, the Universe, and Everything, but it is close."
    )

    for i, x in enumerate(calculate(100)):
        print(f"{i + 1}. {x[0]}: {x[1]}")
