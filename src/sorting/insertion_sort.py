# O(N^2)
def insertion_sort(a: list[int]) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        # Ставим элемент на его место
        while j > 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
