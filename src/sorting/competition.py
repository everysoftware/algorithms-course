from .quick_select import quick_select


# O(N) in average
def competition(scores: list[int]) -> float:
    n = len(scores)
    if n % 2 == 1:
        # Если количество элементов нечетное, возвращаем средний элемент
        return quick_select(scores, n // 2 + 1)
    else:
        # Если количество элементов четное, возвращаем среднее двух средних элементов
        left = quick_select(scores, n // 2)
        right = quick_select(scores, n // 2 + 1)

        return round((left + right) / 2, 6)
