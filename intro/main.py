from fib import test_fib
from gcd import test_gcd
from bigo import test_bigo


if __name__ == '__main__':
    task = {
        'fib': test_fib,
        'gcd': test_gcd,
        'bigo': test_bigo
    }
    task[input()]()
