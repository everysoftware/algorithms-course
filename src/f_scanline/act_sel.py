# O(n log n)
def act_sel(acts: list[tuple[int, int]]) -> list[tuple[int, int]]:
    n = len(acts)
    # Сортируем заявки по правому концу отрезка.
    acts.sort(key=lambda x: x[1])
    selection = []
    i = 0
    while i < n:
        act = acts[i]
        # Добавляем в решение заявку.
        selection.append(act)
        # Пропускаем все заявки, которые пересекаются с текущей.
        while i < n and acts[i][0] < act[1]:
            i += 1
    return selection
