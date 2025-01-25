from src.l_dp2.edit_distance import edit_distance_dp


# O(q * n * m), где q - количество слов, n - длина строки a, m - длина строки b
def edit_candidates(a: str, words: list[str]) -> tuple[int, list[str]]:
    distances = [edit_distance_dp(a, word) for word in words]
    min_distance = min(distances)
    result = [word for word, distance in zip(words, distances) if distance == min_distance]
    return min_distance, result
