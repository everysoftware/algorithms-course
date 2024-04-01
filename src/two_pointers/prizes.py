"""
На основе: https://leetcode.com/problems/maximize-win-from-two-segments/description/

Дан отсортированный по неубыванию массив позиций призов на прямой OX и число k.
Определить максимальное количество призов, которое можно выйграть, выбрав отрезок длиной k.

Пример: prize_positions = [1,1,2,2,3,3,5], k = 2
Ответ: 6
Пояснение: Можно выбрать призы на отрезке [1, 3], их количество составит 6.
"""


def prizes(prize_positions: list[int], k: int) -> int:
    """Решает задачу методом двух указателей. Сложность O(N)."""
    n = len(prize_positions)

    left, right = 0, 0
    ans = 0

    while right < n:
        # Если текущий приз в пределах k от первого приза в окне, просто увеличиваем правый указатель
        if (
            prize_positions[right] - prize_positions[left] <= k
            or right - left <= k
        ):
            right += 1
        # Иначе, если в окне уже есть k+1 призов, увеличиваем левый указатель
        else:
            left += 1
        # Обновляем максимальное количество призов
        ans = max(ans, right - left)

    return ans
