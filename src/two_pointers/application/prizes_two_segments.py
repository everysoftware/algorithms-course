"""
https://leetcode.com/problems/maximize-win-from-two-segments/description/

Дан отсортированный по неубыванию массив позиций призов на прямой OX и число k.
Определить максимальное количество призов, которое можно выйграть, выбрав 2 отрезка длиной k.

Пример: prize_positions = [1,1,2,2,3,3,5], k = 2
Ответ: 7.
Пояснение: Можно выбрать призы на отрезке [1, 3], их количество составит 5,
а также призы на отрезке [3, 5], их количество составит 2, в сумме 7.
"""


def prizes_two_segments(prize_positions: list[int], k: int) -> int:
    """Решает задачу методом двух указателей. Сложность O(N)."""
    n = len(prize_positions)

    # Максимальное число призов для первых i призов
    d = [0] * (n + 1)

    left, ans = 0, 0
    for right in range(1, n + 1):
        # Пока разница между концами отрезка больше k, сдвигаем левый конец
        while prize_positions[right - 1] - prize_positions[left] > k:
            left += 1

        # Считаем число призов в текущем отрезке
        prizes = right - left

        # Обновляем максимальное число призов
        d[right] = max(d[right - 1], prizes)

        # Обновляем ответ: выбираем первым самый лучший отрезок до left,
        # а вторым текущий отрезок от left до right.
        ans = max(ans, d[left] + prizes)

    return ans
