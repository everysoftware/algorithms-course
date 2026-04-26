import heapq


# O(n log n)
def huffman_encode(s: str) -> tuple[str, dict[str, str]]:
    result = ""
    tree = huffman_tree(s)
    for c in s:
        result += tree[c]
    return result, tree


# O(n)
def huffman_decode(s: str, tree: dict[str, str]) -> str:
    result = ""
    code = ""
    for c in s:
        code += c
        if code in tree:
            result += tree[code]
            code = ""
    return result


# O(n log n)
def huffman_tree(s: str) -> dict[str, str]:
    # Считаем частоту встречаемости каждого символа в строке.
    freq = count_chars(s)
    # Создаем кучу: каждый элемент очереди представляет собой кортеж (частота, символ).
    queue = [(v, k) for k, v in freq.items()]
    heapq.heapify(queue)
    # Создаем словарь для хранения кодов Хаффмана.
    tree = {c: "" for c in freq}
    # Если в строке есть только один символ, то кодируем его как "0".
    if len(freq) == 1:
        tree[s[0]] = "0"
    # Пока в очереди есть хотя бы два узла.
    while len(queue) >= 2:
        # Извлекаем два узла с минимальной частотой - их нужно закодировать в первую очередь.
        left = extract_min(queue)
        right = extract_min(queue)
        # Добавляем новый узел в очередь:
        # его название равно конкатенации названий двух извлеченных узлов (a + b = ab),
        # а его частота равна сумме частот двух извлеченных узлов (1 + 2 = 3).
        queue.append((left[0] + right[0], left[1] + right[1]))
        # Обновляем предков: добавляем "0" к коду левого узла и "1" к коду правого узла.
        for ancestor in left[1]:
            tree[ancestor] = "0" + tree[ancestor]
        for ancestor in right[1]:
            tree[ancestor] = "1" + tree[ancestor]
    return tree


# O(n)
def count_chars(s: str) -> dict[str, int]:
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    return freq


# O(log n)
def extract_min(queue: list[tuple[int, str]]) -> tuple[int, str]:
    return heapq.heappop(queue)
