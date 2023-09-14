# Модуль 1. Введение

## Содержание

[1.1. Числа Фибоначчи](https://github.com/everysoftware/CSC_Algorithms/tree/master/CSC_Algorithms_Intro#11-%D1%87%D0%B8%D1%81%D0%BB%D0%B0-%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8)  
[1.2. Наибольшой общий делитель](https://github.com/everysoftware/CSC_Algorithms/tree/master/CSC_Algorithms_Intro#12-%D0%BD%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9-%D0%BE%D0%B1%D1%89%D0%B8%D0%B9-%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C)  
[1.3. O-символика](https://github.com/everysoftware/CSC_Algorithms/tree/master/CSC_Algorithms_Intro#13-o-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%B8%D0%BA%D0%B0)  

## 1.1. Числа Фибоначчи

Файл: ```fib.py```
### Вычисление числа Фибоначчи через рекурсию
```python
def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)
```
### Вычисление числа Фибоначчи с кэшированием (lru_cache)
```python
from functools import lru_cache


@lru_cache(None)
def fib_rec_cached(n):
    if n < 2:
        return n
    else:
        return fib_rec_cached(n - 1) + fib_rec_cached(n - 2)
```
### [Вычисление числа Фибоначчи с помощью таблицы](https://stepik.org/lesson/13228/step/6?unit=3414)
```python
def fib_table(n):
    if n < 2:
        return n
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]
  ```
### Вычисление числа Фибоначчи с сохранением только последних двух чисел
```python
def fib_two_last(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1 + fib2
```
### Вычисление приближенного значения числа Фибоначчи с помощью формулы
```python
def fib_approximate_formula(n):
    return 1.618 ** n / 5 ** 0.5
```
### Вычисление числа Фибоначчи с помощью формулы
```python
def fib_formula(n):
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    return int((phi ** n - psi ** n) / 5 ** 0.5)
```
### [Вычисление последней цифры числа Фибоначчи](https://stepik.org/lesson/13228/step/7?unit=3414)
```python
def fib_last_digit(n):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, (fib1 + fib2) % 10
    return (fib1 + fib2) % 10
```
### Вычисление числа Фибоначчи по модулю с помощью двух последних чисел
```python
def fib_mod_two_last(n, m):
    if n < 2:
        return n
    fib1 = 0
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, (fib1 + fib2) % m
    return (fib1 + fib2) % m
```
### [Вычисление числа Фибоначчи по модулю методом Пизано](https://stepik.org/lesson/13228/step/8?unit=3414)
```python
def fib_mod_pisano(n, m):
    # Используем периодичность.
    if n < 2:
        return n
    a = [0] * (6 * m + 2)
    a[1] = 1
    a[2] = a[0] + a[1]
    i = 3
    while a[i - 1] != 1 or a[i - 2] != 0:
        a[i] = (a[i - 1] + a[i - 2]) % m
        i += 1
    return a[n % (i - 2)]
```


## 1.2. Наибольшой общий делитель

Файл: ```gcd.py```
### Наивный алгоритм НОД
```python
def gcd_naive(x, y):
    res = 1
    for d in range(2, max(x, y)):
        if x % d == 0 and y % d == 0:
            res = d
    return res
```
### Рекурсивная реализация алгоритма Евклида
```python
"""
Пусть a >= b > 0 и r - остаток от деления a на b. Тогда
НОД(a, b) = НОД(r, b). Это следует из равенства: НОД(a, b) = НОД(a - b, b).
Временная сложность: O(log(ab))
"""


def gcd_euclid(a, b):
    if a == 0 or b == 0:
        return 0
    elif a > b:
        return gcd_euclid(a % b, b)
    else:
        return gcd_euclid(a, b % a)


# Вариант покороче.
def gcd(a, b):
    return gcd(b, a % b) if b else a
```
### [Циклическая реализация алгоритма Евклида](https://stepik.org/lesson/13229/step/5?unit=3415)
```python
def gcd_non_rec(a, b):
    while b:
        a, b = b, a % b
    return a
```
## 1.3. O-символика

Файл: ```bigo.py```
### [Сортировка функций по скорости роста](https://stepik.org/lesson/13230/step/10?unit=3416)
```python
from math import log, sqrt, factorial


def calculate(n):
    return {
        # '2^(2^n)': 2 ** (2 ** n)
        # 'n!': factorial(n),
        # '2^3n': 2 ** (3 * n),
        # '4^n': 4 ** n,
        # '2^n': 2 ** n,
        # 'n^sqrt(n)': n ** sqrt(n),
        'n^2': n ** 2,
        'sqrt(n)': sqrt(n),
        'log^2(n)': log(n, 2) ** 2,
        '7^log(n)': 7 ** log(n, 2),
        'n^log(n)': n ** log(n, 2),
        '3^log(n)': 3 ** log(n, 2),
        'log(log(n))': log(log(n, 2), 2),
        'log(n)^log(n)': log(n, 2) ** log(n, 2),
        'n/log(n)': n / log(n, 5),
        'sqrt(log(n))': sqrt(log(n, 4)),
        'log(n!)': log(factorial(n), 2),
        'log(n)': log(n, 3)
    }


def test_bigo():
    f = calculate(100_000)
    print('Top functions:')
    for i, x in enumerate(sorted(f, key=lambda key: f[key])):
        print(str(i + 1) + ')', x, 'with result:', f[x])
```
