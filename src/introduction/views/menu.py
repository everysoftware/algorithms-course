from common.menu_factory import menu_factory
from .tasks import solve_fib, solve_fib_last_digit, solve_fib_mod, solve_gcd

menu = menu_factory(
    "Intro",
    [
        ("N-th Fibonacci number", solve_fib),
        ("Last digit of N-th Fibonacci number", solve_fib_last_digit),
        ("N-th Fibonacci number modulo", solve_fib_mod),
        ("Greatest Common Divisor", solve_gcd),
    ],
)
