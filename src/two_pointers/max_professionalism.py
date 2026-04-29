# O(n)
def max_professionalism(p: list[int]) -> int:
    n = len(p)
    high, curr, ans = 0, 0, 0
    for low in range(n):
        # Добавляем игрока high в команду, пока это возможно
        while high < n and (low == high or p[low] + p[low + 1] >= p[high]):
            curr += p[high]
            high += 1
        ans = max(ans, curr)
        # Выкидываем игрока low из команды.
        curr -= p[low]
    return ans
