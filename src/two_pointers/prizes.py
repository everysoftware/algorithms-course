# O(n)
def prizes(prize_positions: list[int], k: int) -> int:
    n = len(prize_positions)
    low, ans = 0, 0
    for high in range(n):
        # Сдвигаем левый указатель, пока не удовлетворим условие
        while prize_positions[high] - prize_positions[low] > k:
            low += 1
        ans = max(ans, high - low + 1)
    return ans
