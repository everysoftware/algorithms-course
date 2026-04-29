# O(n log n)
def job_scheduling(start_time: list[int], end_time: list[int], profit: list[int]) -> int:
    n = len(start_time)
    events = []
    for i in range(n):
        events.append((start_time[i], 1, i))
        events.append((end_time[i], 0, i))
    events.sort()
    dp = [0] * n
    mx = 0
    for _, t, i in events:
        # Если это начало задачи, то высчитываем максимальный профит, используя текущий максимум
        if t == 1:
            dp[i] = mx + profit[i]
        # Если это конец задачи, то обновляем максимум
        else:
            mx = max(mx, dp[i])
    return mx
