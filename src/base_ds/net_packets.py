from collections import deque


# O(n)
def net_packets(n: int, packets: list[tuple[int, int]], size: int) -> list[int]:
    queue: deque[int] = deque()
    start_times = []
    for i, (arrival, duration) in enumerate(packets):
        # Удаляем из очереди пакеты, которые уже обработаны
        while queue and queue[0] <= arrival:
            queue.popleft()
        if len(queue) == size:
            # Если буфер полон, то пакет отбрасывается
            start_times.append(-1)
        else:
            # Если буфер не полон, то пакет добавляется в очередь
            start_time = max(queue[-1] if queue else arrival, arrival)
            start_times.append(start_time)
            queue.append(start_time + duration)
    return start_times
