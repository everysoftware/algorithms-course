from src.i_dnc.kth_largest import quick_select


# O(N) в среднем, O(N^2) в худшем
def median_salary(scores: list[int]) -> float:
    n = len(scores)
    if n % 2 == 1:
        # Если количество элементов нечетное, вернуть средний элемент
        return quick_select(scores, n // 2 + 1)
    else:
        # Если количество элементов четное, вернуть среднее двух средних элементов
        left = quick_select(scores, n // 2)
        right = quick_select(scores, n // 2 + 1)
        median = (left + right) / 2
        return round(median, 6)
