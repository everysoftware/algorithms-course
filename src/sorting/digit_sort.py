from .counting_sort import counting_sort


# O(D), D - number of digits
def get_d(x: int) -> int:
    d = 0
    while x > 0:
        d += 1
        x //= 10
    return d


# O(DN), D - max number of digits
def digit_sort(a: list[int]) -> list[int]:
    d = get_d(max(a))
    power = 1

    for _ in range(d):
        # Сортировка по текущему разряду
        a = counting_sort(a, 9, key=lambda x: (x // power) % 10)
        # Переход к следующему разряду
        power *= 10

    return a
