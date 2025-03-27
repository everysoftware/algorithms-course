import heapq


def build_tree(s: str) -> dict[str, str]:
    # составляем словарь частотности
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    if len(d) == 1:
        return {s[0]: "0"}
    # составляем очередь
    q = [(v, k) for k, v in d.items()]
    heapq.heapify(q)
    tree = {}
    # кодирование
    while len(q) >= 2:
        # достаем первые 2 элемента из очереди
        v1, c1 = heapq.heappop(q)
        v2, c2 = heapq.heappop(q)
        # добавляем новый элемент
        v3 = v1 + v2
        c3 = c1 + c2
        heapq.heappush(q, (v3, c3))
        # рассматриваем левый узел
        for c in c1:
            if c not in tree:
                tree[c] = ""
            tree[c] += "0"
        # рассматриваем правый узел
        for c in c2:
            if c not in tree:
                tree[c] = ""
            tree[c] += "1"
    return tree


def huffman(s: str) -> tuple[str, dict[str, str]]:
    tree = build_tree(s)
    result = ""
    for c in s:
        result += tree[c]
    return result, tree
