# O(n)
def null_exchange(a: list[int]) -> int:
    count = 0
    # prefix_sums[i] - количество периодов, когда сумма транзакций равна i.
    p: dict[int, int] = {}
    curr_sum = 0
    for num in a:
        # Обновляем текущую сумму
        curr_sum += num
        # Если текущая сумма равна нулю, то увеличиваем счетчик на один
        if curr_sum == 0:
            count += 1
        # Если текущая сумма уже встречалась ранее, то увеличиваем счетчик на количество ее появлений
        if curr_sum in p:
            count += p[curr_sum]
        # Добавляем текущую сумму в словарь или увеличиваем ее счетчик на один
        p[curr_sum] = p.get(curr_sum, 0) + 1
    return count
