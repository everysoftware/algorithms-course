from collections import deque


# O(NM)
def average_waiting_time(n: int, clients: list[tuple[int, int]]) -> float:
    queue = deque(clients)
    windows = [0] * n  # Время окончания обслуживания в каждом окне
    total_waiting_time = 0

    while queue:
        arrival_time, service_time = queue.popleft()
        # Берем окно, которое освободится раньше всего
        min_service_end_time = min(windows)
        window_index = windows.index(min_service_end_time)

        # Если клиент пришел до окончания обслуживания другого клиента в этом окне
        if arrival_time < min_service_end_time:
            total_waiting_time += min_service_end_time - arrival_time
            # Новое время окончания обслуживания в этом окне
            new_service_end_time = min_service_end_time + service_time
        else:
            # Новое время окончания обслуживания в этом окне
            new_service_end_time = arrival_time + service_time

        # Обновляем время окончания обслуживания в этом окне
        windows[window_index] = new_service_end_time

    return round(total_waiting_time / len(clients), 6)
