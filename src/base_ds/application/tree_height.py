# RecursionError: maximum recursion depth exceeded
# O(N^2)
def tree_height_re(a, r):
    height = 1
    children = [i for i, j in enumerate(a) if j == r]
    for c in children:
        height = max(height, tree_height_re(a, c) + 1)
    return height


# O(N)
def tree_height(a):
    n = len(a)
    r = -1
    children = {i: [] for i in range(n)}
    for i in range(n):
        if a[i] == -1:
            r = i
        else:
            children[a[i]].append(i)
    # DFS.
    # d[i] - высота дерева заканчивающегося в i-й вершине
    d = [0] * n
    st, path = [r], set()
    while st:
        v = st.pop()
        if v not in path:
            d[v] += 1
            path.add(v)
            for c in children[v]:
                st.append(c)
                d[c] += d[v]
    return max(d)
