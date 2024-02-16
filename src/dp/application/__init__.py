"""
Динамическое программирование.

Общие принципы:
1. Понимать, что мы вычисляем
2.
"""

from .calculator import calculator
from .fib import fib_cache, fib_dp, fib_lru_cache
from .ladder import ladder
from .grades import grades

__all__ = ["fib_cache", "fib_dp", "fib_lru_cache", "ladder", "calculator", "grades"]
