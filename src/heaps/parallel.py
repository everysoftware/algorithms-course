import heapq


def parallel(n: int, m: int, time: list[int]) -> list[tuple[int, int]]:
    result = []
    h: list[tuple[int, int]] = []
    for i in range(n):
        heapq.heappush(h, (0, i))
    for i in range(m):
        t = time[i]
        x = heapq.heappop(h)
        result.append((x[1], x[0]))
        heapq.heappush(h, (x[0] + t, x[1]))
    return result
