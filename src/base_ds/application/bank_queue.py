"""
В банке работает n окон для обслуживания клиентов. Клиенты приходят в банк и становятся в очередь.
Каждый клиент обслуживается за определенное время. Необходимо определить, сколько времени в среднем придется
ждать клиенту перед началом обслуживания.
"""

from collections import deque


def average_waiting_time(n: int, clients: list[tuple[int, int]]) -> float:
    """Решает задачу о среднем времени ожидания клиента перед началом обслуживания. Сложность: O(NM)."""
    queue = deque(clients)
    windows = [0] * n  # Время окончания обслуживания в каждом окне
    total_waiting_time = 0

    while queue:
        arrival_time, service_time = queue.popleft()
        # Берем окно, которое освободится раньше всего
        min_service_end_time = min(windows)
        window_index = windows.index(min_service_end_time)

        # Если клиент пришел до окончания обслуживания в этом окне
        if arrival_time < min_service_end_time:
            total_waiting_time += min_service_end_time - arrival_time
            # Новое время окончания обслуживания в этом окне
            new_service_end_time = min_service_end_time + service_time
        else:
            # Новое время окончания обслуживания в этом окне
            new_service_end_time = arrival_time + service_time

        # Обновляем время окончания обслуживания в этом окне
        windows[window_index] = new_service_end_time

    return total_waiting_time / len(clients)
