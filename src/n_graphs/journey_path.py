Flight = tuple[str, str]


# сложность O(N), по памяти O(N)
def get_route(flights: list[Flight]) -> list[str]:
    # Строим неориентированный граф
    neighbors: dict[str, set[str]] = {}
    for a, b in flights:
        if a not in neighbors:
            neighbors[a] = set()
        if b not in neighbors:
            neighbors[b] = set()
        neighbors[a].add(b)
        neighbors[b].add(a)
    # Определяем стартовую точку
    start: str = ""
    for city, city_neighbors in neighbors.items():
        if len(city_neighbors) == 1:
            start = city
            break
    # Обходим дерево
    path: list[str] = []
    visited: set[str] = set()
    while len(path) != len(neighbors):
        path.append(start)
        visited.add(start)
        for candidate in neighbors[start]:
            if candidate not in visited:
                start = candidate
                break
    return path


# Более чистая версия
def get_route_enhanced(flights: list[Flight]) -> list[str]:
    # Строим неориентированный граф
    neighbors: dict[str, set[str]] = {}
    for a, b in flights:
        if a not in neighbors:
            neighbors[a] = set()
        if b not in neighbors:
            neighbors[b] = set()
        neighbors[a].add(b)
        neighbors[b].add(a)
    # Определяем стартовую точку
    start = next(city for city, neigh in neighbors.items() if len(neigh) == 1)
    # Обходим граф
    path: list[str] = [start]
    prev: str | None = None
    # городов на 1 больше, чем перелетов
    while len(path) <= len(flights):
        current = path[-1]
        # Находим следующего соседа
        for nxt in neighbors[current]:
            if nxt != prev:
                path.append(nxt)
                prev = current
                break
    return path
